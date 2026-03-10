const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: true,
    proxy: {
      server: 'socks5://127.0.0.1:1080'
    },
    args: ['--disable-dev-shm-usage']
  });

  const context = await browser.newContext();
  const page = await context.newPage();

  const creds = {
    login: process.env.YA_LOGIN || 'directskif',
    password: process.env.YA_PASSWORD || 'PIvjb2g2bnvk'
  };

  try {
    await page.goto('https://direct.yandex.ru/', { waitUntil: 'domcontentloaded', timeout: 60000 });

    if (await page.locator('#passp-field-login').count() === 0) {
      const loginButton = page.locator('a.Button2, button[data-t="button:action-button"], button[type="button"]');
      if (await loginButton.count() > 0) {
        await loginButton.first().click();
      }
      await page.waitForSelector('#passp-field-login', { timeout: 20000 });
    }

    await page.fill('#passp-field-login', creds.login);
    await page.click('button[type="submit"]');

    await page.waitForSelector('#passp-field-passwd', { timeout: 20000 });
    await page.fill('#passp-field-passwd', creds.password);
    await page.click('button[type="submit"]');

    await page.waitForLoadState('networkidle');
    await page.waitForTimeout(5000);

    await page.screenshot({ path: 'output/yandex-direct-after-login.png', fullPage: true });

    console.log('Login flow attempted. Screenshot saved at output/yandex-direct-after-login.png');
  } catch (error) {
    console.error('Login attempt failed:', error);
    await page.screenshot({ path: 'output/yandex-direct-error.png', fullPage: true }).catch(() => {});
    process.exitCode = 1;
  } finally {
    await browser.close();
  }
})();
