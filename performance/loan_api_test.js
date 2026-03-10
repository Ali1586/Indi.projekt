import http from 'k6/http';
import { check, sleep } from 'k6';

const BASE_URL = 'https://souderbroder-loan-lab.lovable.app/api';
const HEADERS = {
  'Authorization': 'Bearer 0ae0909526eb8f6563dfac7e6b3a7523aa68bdac57fa7590aae3c9762a99ff25',
  'Content-Type': 'application/json',
};

export const options = {
  vus: 5,
  duration: '20s',
  thresholds: {
    http_req_duration: ['p(95)<2000'],
    http_req_failed: ['rate<0.05'],
  },
};

export default function () {
  const get = http.get(`${BASE_URL}/loans`, { headers: HEADERS });
  check(get, {
    'GET /loans – 200':       (r) => r.status === 200,
    'GET /loans – är lista':  (r) => Array.isArray(JSON.parse(r.body)),
  });

  sleep(1);

  const post = http.post(`${BASE_URL}/loans`, JSON.stringify({
    name: 'Test Person',
    ssn: '196408233234',
    amount: 10000,
    interestRate: 5.5,
    email: 'test@example.com',
  }), { headers: HEADERS });

  check(post, {
    'POST /loans – 200/201':    (r) => r.status === 200 || r.status === 201,
    'POST /loans – har id':     (r) => JSON.parse(r.body).id !== undefined,
  });

  sleep(1);
}