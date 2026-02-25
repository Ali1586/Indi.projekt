import http from 'k6/http';
import { check, sleep } from 'k6';

export default function () {
  // Ersätt med din faktiska URL (t.ex. http://localhost:5000/api/loans)
  const response = await page.goto('https://souderbroder-loan-lab.lovable.app/loan');

    check(response, {
      'Status är 200 (OK)': (r) => r.status() === 200,
    });

}