const http = require('http');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const PORT = 4173;
const CSV_FILE = path.join(__dirname, '..', 'expenses_2026.csv');
const EXPORT_SCRIPT = path.join(__dirname, '..', '..', 'scripts', 'export_expenses_data.py');

const mimeTypes = {
  '.html': 'text/html',
  '.js': 'text/javascript',
  '.css': 'text/css',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
};

const server = http.createServer((req, res) => {
  if (req.method === 'POST' && req.url === '/api/add-expense') {
    let body = '';
    req.on('data', chunk => {
      body += chunk.toString();
    });
    req.on('end', () => {
      try {
        const data = JSON.parse(body);
        const line = `\n${data.date},${data.vendor},${data.category},${data.subcategory},${data.item},1,${data.price},${data.price},,${data.payment_method},,${data.notes}`;
        
        fs.appendFileSync(CSV_FILE, line, 'utf8');
        
        const cwdPath = path.join(__dirname, '..', '..');
        exec(`python3 scripts/export_expenses_data.py`, { cwd: cwdPath }, (error, stdout, stderr) => {
          if (error) {
            console.error(`Export script error: ${error.message}`);
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ success: false, error: 'Failed to update dashboard data.' }));
            return;
          }
          res.writeHead(200, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ success: true }));
        });
      } catch (err) {
        console.error(err);
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: false, error: 'Invalid payload.' }));
      }
    });
    return;
  }

  // Serve static files
  let reqUrl = req.url.split('?')[0];
  if (reqUrl === '/') reqUrl = '/index.html';
  
  let filePath = path.join(__dirname, reqUrl);
  
  // Specific override for expenses-data.js which is generated up one level
  if (reqUrl === '/expenses-data.js') {
      filePath = path.join(__dirname, '..', 'expenses-data.js');
  }

  const extname = String(path.extname(filePath)).toLowerCase();
  const contentType = mimeTypes[extname] || 'application/octet-stream';

  fs.readFile(filePath, (error, content) => {
    if (error) {
      if (error.code == 'ENOENT') {
        res.writeHead(404);
        res.end('Not found\n');
      } else {
        res.writeHead(500);
        res.end('Server Error: ' + error.code + '\n');
      }
    } else {
      res.writeHead(200, { 'Content-Type': contentType });
      res.end(content, 'utf-8');
    }
  });
});

server.listen(PORT, () => {
  console.log(`Finance Dashboard API Server running on port ${PORT}...`);
});
