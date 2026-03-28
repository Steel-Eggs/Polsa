const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  // Width needs to be large enough for 64 leaves * 200px = 12800px.
  await page.setViewport({ width: 14000, height: 1600, deviceScaleFactor: 2 });
  
  // BW tree
  await page.goto('file:///root/.openclaw/workspace/tree_v4_bw.html', {waitUntil: 'networkidle2'});
  const elBw = await page.$('.tree');
  await elBw.screenshot({path: '/root/.openclaw/workspace/tree_v4_bw.png'});

  await browser.close();
})();
