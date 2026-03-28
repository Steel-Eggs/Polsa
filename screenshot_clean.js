const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 2000, height: 1200, deviceScaleFactor: 2 });
  await page.goto('file:///root/.openclaw/workspace/family_tree_clean.html', {waitUntil: 'networkidle2'});
  const element = await page.$('.tree');
  await element.screenshot({path: '/root/.openclaw/workspace/family_tree_clean.png', omitBackground: true});
  await browser.close();
})();
