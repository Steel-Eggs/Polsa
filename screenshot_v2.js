const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  // BW tree
  await page.setViewport({ width: 3500, height: 1200, deviceScaleFactor: 2 });
  await page.goto('file:///root/.openclaw/workspace/tree_bw.html', {waitUntil: 'networkidle2'});
  const elBw = await page.$('.tree');
  await elBw.screenshot({path: '/root/.openclaw/workspace/tree_bw.png'});

  // Color tree
  await page.goto('file:///root/.openclaw/workspace/tree_color.html', {waitUntil: 'networkidle2'});
  const elColor = await page.$('.tree');
  await elColor.screenshot({path: '/root/.openclaw/workspace/tree_color.png'});

  await browser.close();
})();
