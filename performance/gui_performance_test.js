import { browser } from 'k6/browser';
import { check } from 'k6';

export const options = {
  scenarios: {
    gui: {
      executor: 'constant-vus',
      vus: 3,
      duration: '20s',
      options: { browser: { type: 'chromium' } },
    },
  },
  thresholds: {
    browser_web_vital_lcp: ['p(95)<4000'],
  },
};

export default async function () {
  const context = await browser.newContext();
  const page = await context.newPage();
  try {
    const r1 = await page.goto('https://souderbroder-loan-lab.lovable.app', { waitUntil: 'networkidle' });
    check(r1, { 'Startsidan – 200': (r) => r && r.status() === 200 });

    const r2 = await page.goto('https://souderbroder-loan-lab.lovable.app/loan', { waitUntil: 'networkidle' });
    check(r2, { 'Lånesidan – 200': (r) => r && r.status() === 200 });
  } finally {
    await page.close();
    await context.close();
  }
}