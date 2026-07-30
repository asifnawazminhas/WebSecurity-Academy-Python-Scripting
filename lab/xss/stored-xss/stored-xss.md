# Manual Solution Using Burp Suite Community

## Lab

**Stored DOM XSS**

> **Note:** Replace the lab URL below with your own PortSwigger Web Security Academy lab instance.

### Blog Post

```text
https://0a8200ba03eb44e181c944a700ad00cc.web-security-academy.net/post?postId=1
```

### Injection Point

```text
Comment
```

### Payload

```html
><<img src=1 onerror=alert(1)>
```

### Result

1. Open the blog post.
2. Click **Leave a comment**.
3. Enter the payload in the **Comment** field.
4. Fill in the remaining required fields (Name and Email).
5. Submit the comment.
6. Reload or revisit the blog post.

The stored comment is inserted into the DOM without proper sanitisation, causing the JavaScript payload to execute and the lab to be solved.

---

## Python Implementation

The accompanying Python script:

- Retrieves the CSRF token.
- Submits the XSS payload as a blog comment.
- Reloads the blog post.

```text
stored-dom-xss.py
```
