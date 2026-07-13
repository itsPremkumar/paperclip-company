#!/usr/bin/env node

/**
 * agent-config-generator
 * ------------------------
 * Interactive CLI that generates ready-to-use Paperclip agent configuration
 * JSON files.  Companion to the "Full Autonomous Company Starter Kit" blueprint
 * by Prem Autonomous Co.
 *
 * @license MIT
 * @author Prem Autonomous Co <https://premautonomous.co>
 * @package agent-config-generator
 */

import inquirer from 'inquirer';
import { writeFile, constants } from 'node:fs/promises';
import { access } from 'node:fs/promises';
import { existsSync, mkdirSync } from 'node:fs';
import path from 'node:path';
import { createInterface } from 'node:readline';
import { fileURLToPath } from 'node:url';

// ---------------------------------------------------------------------------
// Constants
// ---------------------------------------------------------------------------

/** @type {string} */
const VERSION = '1.0.0';

/** @type {string} */
const CLI_NAME = 'gen-agent';

/** @type {string} */
const PAPERCLIP_API_ENDPOINT = 'POST /api/companies/:companyId/agents';

/** @type {string} */
const PREMIUM_URL = 'https://premautonomous.co/products/agent-config-generator';

/**
 * Known adapter types supported by Paperclip.
 * @type {readonly string[]}
 */
const ADAPTER_TYPES = /** @type {const} */ ([
  'hermes_local',
  'openai_assistant',
  'anthropic',
  'custom_api',
]);

/**
 * Role options for generated agents.
 * @type {readonly string[]}
 */
const ROLES = /** @type {const} */ ([
  'engineer',
  'cto',
  'researcher',
  'writer',
  'analyst',
  'architect',
  'product-manager',
  'custom',
]);

/**
 * Model identifier presets.
 * @type {readonly {name: string, value: string}[]}
 */
const MODEL_PRESETS = /** @type {const} */ ([
  { name: 'DeepSeek V4 (tencent/hy3:free)     — Free, fast, general purpose', value: 'tencent/hy3:free' },
  { name: 'Claude 3 Haiku (anthropic)         — Fast & affordable', value: 'anthropic/claude-3-haiku' },
  { name: 'Claude 3.5 Sonnet (anthropic)      — Best-in-class coding', value: 'anthropic/claude-sonnet-4-20250514' },
  { name: 'GPT-4o (openai)                    — Strong all-rounder', value: 'openai/gpt-4o' },
  { name: 'Gemini 2.0 Flash (google)          — Speed demon', value: 'google/gemini-2.0-flash-exp' },
  { name: 'Custom model ID                     — Enter any model string', value: '__custom__' },
]);

/**
 * Provider options.
 * @type {readonly {name: string, value: string}[]}
 */
const PROVIDER_OPTIONS = /** @type {const} */ ([
  { name: 'OpenRouter    — Unified API, many models', value: 'openrouter' },
  { name: 'Anthropic     — Claude models direct', value: 'anthropic' },
  { name: 'OpenAI        — GPT models direct', value: 'openai' },
  { name: 'Google AI     — Gemini models direct', value: 'google' },
  { name: 'Custom        — Self-hosted / other', value: 'custom' },
]);

/**
 * Available tool sets.
 * @type {readonly {name: string, value: string, checked: boolean}[]}
 */
const TOOLSET_OPTIONS = /** @type {const} */ ([
  { name: 'terminal  — Shell / CLI execution', value: 'terminal', checked: true },
  { name: 'file      — Read & write files', value: 'file', checked: true },
  { name: 'web       — HTTP requests, browsing', value: 'web', checked: true },
  { name: 'memory    — Long-term knowledge store', value: 'memory', checked: false },
  { name: 'search    — Semantic & keyword search', value: 'search', checked: false },
  { name: 'github    — GitHub API integration', value: 'github', checked: false },
  { name: 'gitlab    — GitLab API integration', value: 'gitlab', checked: false },
  { name: 'slack     — Slack messaging', value: 'slack', checked: false },
  { name: 'email     — Send & receive email', value: 'email', checked: false },
  { name: 'browser   — Headless browser automation', value: 'browser', checked: false },
]);

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

/**
 * Print a styled banner to stdout.
 * @returns {void}
 */
function printBanner() {
  console.log('');
  console.log('╔═══════════════════════════════════════════════════════════╗');
  console.log('║          Agent Config Generator  v' + VERSION.padEnd(38) + '║');
  console.log('║     Generate Paperclip agent configs — interactively     ║');
  console.log('║     by Prem Autonomous Co                                ║');
  console.log('╚═══════════════════════════════════════════════════════════╝');
  console.log('');
}

/**
 * Exit with an error message.
 * @param {string} msg
 * @returns {never}
 */
function die(msg) {
  console.error(`\n  ✖ ERROR: ${msg}\n`);
  process.exit(1);
}

/**
 * Validate that a value is a non-empty string.
 * @param {string} input
 * @returns {boolean | string}
 */
function nonEmpty(input) {
  if (typeof input !== 'string' || input.trim().length === 0) {
    return 'This field is required.';
  }
  return true;
}

/**
 * Validate a positive integer string.
 * @param {string} input
 * @returns {boolean | string}
 */
function positiveInt(input) {
  const n = Number(input);
  if (!Number.isInteger(n) || n < 1) {
    return 'Enter a positive integer (e.g. 3, 10, 50).';
  }
  return true;
}

/**
 * Pretty-print JSON with a colour hint (just plain text here).
 * @param {unknown} obj
 * @returns {string}
 */
function formatJSON(obj) {
  return JSON.stringify(obj, null, 2);
}

// ---------------------------------------------------------------------------
// Config builder
// ---------------------------------------------------------------------------

/**
 * @typedef {Object} HeartbeatConfig
 * @property {boolean} enabled
 * @property {number} maxConcurrentRuns
 */

/**
 * @typedef {Object} AdapterConfig
 * @property {string} model
 * @property {string} provider
 * @property {number} maxIterations
 * @property {number} timeoutSec
 * @property {string[]} enabledToolsets
 * @property {HeartbeatConfig} heartbeat
 */

/**
 * @typedef {Object} AgentConfig
 * @property {string} name
 * @property {string} adapterType
 * @property {string} role
 * @property {AdapterConfig} adapterConfig
 */

/**
 * Build an AgentConfig from user answers.
 *
 * @param {Object} answers - Raw inquirer answers
 * @param {string} answers.agentRole
 * @param {string} answers.customRole
 * @param {string} answers.model
 * @param {string} answers.customModel
 * @param {string} answers.provider
 * @param {string} answers.customProvider
 * @param {string[]} answers.toolsets
 * @param {boolean} answers.heartbeatEnabled
 * @param {string} answers.maxConcurrentRuns
 * @returns {AgentConfig}
 */
function buildConfig(answers) {
  const role = answers.agentRole === 'custom'
    ? answers.customRole
    : answers.agentRole;

  const model = answers.model === '__custom__'
    ? answers.customModel
    : answers.model;

  const provider = answers.provider === 'custom'
    ? answers.customProvider
    : answers.provider;

  // Derive a human-friendly agent name from the role. Title-case each
  // hyphen/space separated word so "code-reviewer" → "Code Reviewer".
  const name = role
    .split(/[-\s]+/)
    .filter(Boolean)
    .map((/** @type {string} */ w) => w.charAt(0).toUpperCase() + w.slice(1))
    .join(' ');

  return {
    name: `Paperclip ${name}`,
    adapterType: 'hermes_local',
    role,
    adapterConfig: {
      model,
      provider,
      maxIterations: 50,
      timeoutSec: 1800,
      enabledToolsets: answers.toolsets,
      heartbeat: {
        enabled: answers.heartbeatEnabled,
        maxConcurrentRuns: Number(answers.maxConcurrentRuns),
      },
    },
  };
}

// ---------------------------------------------------------------------------
// Prompts
// ---------------------------------------------------------------------------

/**
 * Run the interactive prompt sequence and return user answers.
 *
 * @returns {Promise<import('inquirer').Answers>}
 */
async function runPrompts() {
  const answers = await inquirer.prompt([
    // ── 1. Agent Role ──────────────────────────────────────────────────────
    {
      type: 'list',
      name: 'agentRole',
      message: 'What role should the agent fill?',
      description: 'The agent\'s job function inside your Paperclip company',
      choices: ROLES.map((r) => ({
        name: r.charAt(0).toUpperCase() + r.slice(1).replace(/-/g, ' '),
        value: r,
      })),
      default: 'engineer',
    },
    {
      type: 'input',
      name: 'customRole',
      message: 'Enter a custom role name:',
      description: 'e.g. "code-reviewer", "devops-bot", "data-pipeline-agent"',
      when: (/** @type {import('inquirer').Answers} */ a) => a.agentRole === 'custom',
      validate: nonEmpty,
    },

    // ── 2. Model ──────────────────────────────────────────────────────────
    {
      type: 'list',
      name: 'model',
      message: 'Which model should power this agent?',
      description: 'The LLM that drives reasoning and tool use',
      choices: MODEL_PRESETS,
      default: 'tencent/hy3:free',
      loop: false,
    },
    {
      type: 'input',
      name: 'customModel',
      message: 'Enter the model ID:',
      description: 'e.g. "mistralai/mistral-large", "meta-llama/llama-3-70b-instruct"',
      when: (/** @type {import('inquirer').Answers} */ a) => a.model === '__custom__',
      validate: nonEmpty,
    },

    // ── 3. Provider ───────────────────────────────────────────────────────
    {
      type: 'list',
      name: 'provider',
      message: 'Which API provider serves this model?',
      description: 'Routes requests to the correct inference backend',
      choices: PROVIDER_OPTIONS,
      default: 'openrouter',
      loop: false,
    },
    {
      type: 'input',
      name: 'customProvider',
      message: 'Enter the provider name:',
      description: 'e.g. "together", "replicate", "ollama", "my-inference-server"',
      when: (/** @type {import('inquirer').Answers} */ a) => a.provider === 'custom',
      validate: nonEmpty,
    },

    // ── 4. Toolsets ───────────────────────────────────────────────────────
    {
      type: 'checkbox',
      name: 'toolsets',
      message: 'Which tools should the agent have access to?',
      description: 'Select all that apply (space to toggle, enter to confirm)',
      choices: TOOLSET_OPTIONS,
      validate: (/** @type {string[]} */ input) => {
        if (input.length === 0) return 'Select at least one toolset.';
        return true;
      },
    },

    // ── 5. Heartbeat ──────────────────────────────────────────────────────
    {
      type: 'confirm',
      name: 'heartbeatEnabled',
      message: 'Enable heartbeat (long-running tasks)?',
      description: 'Lets the agent run tasks in the background',
      default: true,
    },
    {
      type: 'input',
      name: 'maxConcurrentRuns',
      message: 'Max concurrent heartbeat runs:',
      description: 'How many background tasks can run at once',
      default: '3',
      when: (/** @type {import('inquirer').Answers} */ a) => a.heartbeatEnabled === true,
      validate: positiveInt,
    },
  ]);

  return answers;
}

// ---------------------------------------------------------------------------
// Output / Save
// ---------------------------------------------------------------------------

/**
 * Ask the user whether to print, save, or both.
 *
 * @param {AgentConfig} config
 * @returns {Promise<void>}
 */
async function handleOutput(config) {
  const json = formatJSON(config);

  const { action } = await inquirer.prompt([
    {
      type: 'list',
      name: 'action',
      message: 'What would you like to do with the generated config?',
      choices: [
        { name: '📋  Print to console (copy manually)', value: 'print' },
        { name: '💾  Save to file', value: 'save' },
        { name: '📋 + 💾  Both', value: 'both' },
        { name: '❌  Discard (start over)', value: 'discard' },
      ],
    },
  ]);

  if (action === 'discard') {
    console.log('\n  Discarded. Run gen-agent again when ready.\n');
    return;
  }

  if (action === 'print' || action === 'both') {
    console.log('\n' + '─'.repeat(56));
    console.log('  YOUR AGENT CONFIG');
    console.log('─'.repeat(56));
    console.log(json);
    console.log('─'.repeat(56));
    console.log(`\n  POST this to: ${PAPERCLIP_API_ENDPOINT}`);
    console.log(`  Docs: https://docs.paperclip.so/api\n`);
  }

  if (action === 'save' || action === 'both') {
    const { savePath } = await inquirer.prompt([
      {
        type: 'input',
        name: 'savePath',
        message: 'Save path (relative or absolute):',
        default: `paperclip-agent-${config.role}.json`,
        validate: nonEmpty,
      },
    ]);

    const resolved = path.resolve(savePath);
    const dir = path.dirname(resolved);
    if (!existsSync(dir)) {
      mkdirSync(dir, { recursive: true });
    }

    try {
      await writeFile(resolved, json + '\n', 'utf-8');
      console.log(`\n  ✓ Config saved to: ${resolved}\n`);
    } catch (/** @type {unknown} */ err) {
      die(`Could not write file: ${resolved}\n  ${String(err)}`);
    }
  }
}

// ---------------------------------------------------------------------------
// Premium upgrade prompt
// ---------------------------------------------------------------------------

/**
 * Show a premium upsell message after config generation.
 * @returns {void}
 */
function showPremiumUpsell() {
  console.log('');
  console.log('╔═══════════════════════════════════════════════════════════╗');
  console.log('║   🚀  Need multi-agent orchestration?                    ║');
  console.log('║                                                          ║');
  console.log('║   The PRO version ($29) generates a complete            ║');
  console.log('║   Paperclip COMPANY config — multiple agents with        ║');
  console.log('║   inter-agent handoffs, shared memory, and more.        ║');
  console.log('║                                                          ║');
  console.log('║   👉  premium.premautonomous.co                         ║');
  console.log('╚═══════════════════════════════════════════════════════════╝');
  console.log('');
}

// ---------------------------------------------------------------------------
// Help
// ---------------------------------------------------------------------------

/**
 * Print help/usage information.
 * @returns {void}
 */
function printHelp() {
  const helpText = `
  ${CLI_NAME} v${VERSION}  —  Paperclip Agent Config Generator

  USAGE
    ${CLI_NAME}                    Run in interactive mode
    ${CLI_NAME} --help, -h         Show this message
    ${CLI_NAME} --version, -v      Print version

  EXAMPLES
    ${CLI_NAME}
    # Answer 5 prompts → get a ready-to-use Paperclip agent JSON config

  ABOUT
    Generates valid Paperclip agent configurations for use with the
    Paperclip API (POST ${PAPERCLIP_API_ENDPOINT}).

    Part of the "Full Autonomous Company Starter Kit" by Prem Autonomous Co.

    Premium multi-agent orchestration configs:
      ${PREMIUM_URL}
  `;
  console.log(helpText);
}

// ---------------------------------------------------------------------------
// Entry point
// ---------------------------------------------------------------------------

/**
 * Main entry.
 * @param {string[]} args
 * @returns {Promise<void>}
 */
async function main(args) {
  const flag = args[0] ?? '';

  if (flag === '--help' || flag === '-h') {
    printHelp();
    return;
  }

  if (flag === '--version' || flag === '-v') {
    console.log(VERSION);
    return;
  }

  printBanner();

  try {
    const answers = await runPrompts();
    const config = buildConfig(answers);
    await handleOutput(config);
    showPremiumUpsell();
  } catch (/** @type {unknown} */ err) {
    if (err instanceof Error && err.name === 'ExitPromptError') {
      console.log('\n  Cancelled.\n');
      process.exit(0);
    }
    die(String(err));
  }
}

// Only run the CLI when executed directly (not when imported by tests or
// by `prepublishOnly`). This guards against the interactive prompt firing on
// import and lets us export pure functions for unit testing.
const isMain =
  process.argv[1] &&
  fileURLToPath(import.meta.url) === path.resolve(process.argv[1]);

if (isMain) {
  main(process.argv.slice(2)).catch((/** @type {unknown} */ err) => {
    die(String(err));
  });
}

export { buildConfig, printHelp as help, VERSION };
