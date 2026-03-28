const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  await page.goto('file:///root/.openclaw/workspace/tree_v5_bw.html', {waitUntil: 'networkidle2'});
  
  await page.pdf({
    path: '/root/.openclaw/workspace/family_tree_final.pdf',
    width: '17500px',
    height: '2500px',
    printBackground: true,
    pageRanges: '1'
  });

  await browser.close();
})();
