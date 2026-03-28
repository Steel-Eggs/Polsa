const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080 });
  await page.goto('file:///root/.openclaw/workspace/family_tree.html', {waitUntil: 'networkidle2'});
  const element = await page.$('.tree');
  await element.screenshot({path: '/root/.openclaw/workspace/family_tree.png'});
  await browser.close();
})();
