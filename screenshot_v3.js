const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 4500, height: 1500, deviceScaleFactor: 2 });
  
  // BW tree
  await page.goto('file:///root/.openclaw/workspace/tree_v3_bw.html', {waitUntil: 'networkidle2'});
  const elBw = await page.$('.tree');
  await elBw.screenshot({path: '/root/.openclaw/workspace/tree_v3_bw.png'});

  // Color tree
  await page.goto('file:///root/.openclaw/workspace/tree_v3_color.html', {waitUntil: 'networkidle2'});
  const elColor = await page.$('.tree');
  await elColor.screenshot({path: '/root/.openclaw/workspace/tree_v3_color.png'});

  await browser.close();
})();
