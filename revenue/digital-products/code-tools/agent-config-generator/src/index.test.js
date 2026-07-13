#!/usr/bin/env node
/**
 * Unit tests for agent-config-generator core logic.
 * Run with: node --test
 */

import { test } from 'node:test';
import assert from 'node:assert/strict';
import { buildConfig, VERSION } from './index.js';

test('buildConfig derives a human-friendly name with role', () => {
  const cfg = buildConfig({
    agentRole: 'engineer',
    model: 'tencent/hy3:free',
    provider: 'openrouter',
    toolsets: ['terminal', 'file'],
    heartbeatEnabled: true,
    maxConcurrentRuns: '3',
  });
  assert.equal(cfg.name, 'Paperclip Engineer');
  assert.equal(cfg.role, 'engineer');
  assert.equal(cfg.adapterType, 'hermes_local');
  assert.equal(cfg.adapterConfig.model, 'tencent/hy3:free');
  assert.equal(cfg.adapterConfig.provider, 'openrouter');
  assert.deepEqual(cfg.adapterConfig.enabledToolsets, ['terminal', 'file']);
  assert.equal(cfg.adapterConfig.heartbeat.enabled, true);
  assert.equal(cfg.adapterConfig.heartbeat.maxConcurrentRuns, 3);
});

test('buildConfig handles a custom role', () => {
  const cfg = buildConfig({
    agentRole: 'custom',
    customRole: 'code-reviewer',
    model: 'anthropic/claude-sonnet-4-20250514',
    provider: 'anthropic',
    toolsets: ['terminal'],
    heartbeatEnabled: false,
    maxConcurrentRuns: '0',
  });
  assert.equal(cfg.role, 'code-reviewer');
  assert.equal(cfg.name, 'Paperclip Code Reviewer');
  assert.equal(cfg.adapterConfig.heartbeat.enabled, false);
});

test('buildConfig resolves custom model and provider values', () => {
  const cfg = buildConfig({
    agentRole: 'analyst',
    model: '__custom__',
    customModel: 'mistralai/mistral-large',
    provider: 'custom',
    customProvider: 'together',
    toolsets: ['web'],
    heartbeatEnabled: true,
    maxConcurrentRuns: '2',
  });
  assert.equal(cfg.adapterConfig.model, 'mistralai/mistral-large');
  assert.equal(cfg.adapterConfig.provider, 'together');
});

test('VERSION is a semver string', () => {
  assert.match(VERSION, /^\d+\.\d+\.\d+$/);
});
