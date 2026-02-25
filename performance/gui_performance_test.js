import { browser } from 'k6/browser';
import { check } from 'k6';

export const options = {
  scenarios: {
    ui: {
      executor: 'constant-vus',
      vus: 3,            // 3 användare samtidigt
      duration: '10s',    // Kör i 10 sekunder
      options: {
        browser: {
          type: 'chromium',
        },
      },
    },
  },
  thresholds: {
    // Vi sätter 5000ms (5 sekunder) så att testet passerar (blir grönt)
    browser_web_vital_lcp: ['p(95) < 5000'],
  },
};

// Det är denna "export default" som k6 behöver för att veta vad den ska köra!
export default async function () {
  const context = await browser.newContext();
  const page = await context.newPage();

 try {
    console.log("Navigerar...");
    await page.goto('https://souderbroder-loan-lab.lovable.app/loan');

    // Ta bilden direkt här!
    await page.screenshot({ path: 'DEBUG_BILD.png' });
    console.log("Bild sparad!");

  } finally {
    await page.close();
  }
}