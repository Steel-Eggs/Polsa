const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 12000, height: 2000, deviceScaleFactor: 1 });
  await page.goto('file:///root/.openclaw/workspace/family_tree_final.html', {waitUntil: 'networkidle2'});
  const element = await page.$('.tree');
  await element.screenshot({path: '/root/.openclaw/workspace/family_tree_final.png', omitBackground: false});
  await browser.close();
})();
