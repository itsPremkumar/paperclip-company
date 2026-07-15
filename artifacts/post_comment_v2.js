'use strict';
const http = require('http');
const fs = require('fs');
const issueId = process.argv[2];
const body = fs.readFileSync(process.argv[3], 'utf8');
const payload = JSON.stringify({ body: body });
const base = process.env.PAPERCLIP_API_URL.replace(/\/$/, '');
const url = `${base}/api/issues/${issueId}/comments`;
const u = new URL(url);
const req = http.request({
  hostname: u.hostname, port: u.port || 80, path: u.pathname, method: 'POST',
  headers: {
    'Authorization': 'Bearer ' + process.env.PAPERCLIP_API_KEY,
    'X-Paperclip-Run-Id': process.env.PAPERCLIP_RUN_ID,
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(payload)
  }
}, (res) => {
  let d = ''; res.on('data', c => d += c);
  res.on('end', () => console.log('http', res.statusCode, 'resp', d.slice(0, 200)));
});
req.on('error', e => console.log('ERR', e.message));
req.write(payload); req.end();
