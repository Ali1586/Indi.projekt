import http from 'k6/http';
import { check, sleep } from 'k6';

export default function () {
  // Ersätt med din faktiska URL (t.ex. http://localhost:5000/api/loans)
  const res = http.get('http://din-api-url/api/loans');

  check(res, {
    'status är 200': (r) => r.status === 200,
  });

  sleep(1);
}