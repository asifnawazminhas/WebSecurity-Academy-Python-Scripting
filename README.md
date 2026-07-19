# WebSecurity-Academy-Python-Scripting

Python scripting examples for PortSwigger Web Security Academy, focusing on automation, reusable techniques, and practical learning.

> [!IMPORTANT]
> This repository is intended for educational purposes only. The scripts are developed while working through the PortSwigger Web Security Academy and are designed to improve Python scripting and automation skills. Only use these techniques against systems you own or have explicit permission to test.

---

## About

The purpose of this repository is to document my journey of learning Python through the PortSwigger Web Security Academy.

Rather than simply completing labs manually, I focus on writing Python scripts that automate common web application security testing techniques. Each script is designed to reinforce Python fundamentals while building reusable components that can be adapted for future labs.

The emphasis is on understanding how web applications behave, interacting with HTTP requests and responses, and developing practical scripting skills commonly used during authorised penetration testing.

---

## Topics

This repository focuses on scripting examples for the following Web Security Academy topics:

- SQL Injection
- Cross Site Scripting (XSS)
- Cross Site Request Forgery (CSRF)
- Command Injection
- Path Traversal
- File Upload Vulnerabilities
- Server Side Request Forgery (SSRF)
- XML External Entity (XXE) Injection
- JSON Web Token (JWT) Attacks

Not every Web Security Academy topic will be covered. The primary focus is on areas that help strengthen Python scripting and web application testing skills.

---

## Learning Objectives

The goal is to become comfortable writing Python scripts that can:

- Send HTTP GET and POST requests
- Manage sessions and cookies
- Handle authentication
- Parse HTML responses
- Analyse response differences
- Automate repetitive testing tasks
- Build reusable helper functions
- Improve scripting speed for future assessments

This repository is intended as a personal learning resource and a record of progress while improving Python scripting skills.

---

## Repository Structure

```text
WebSecurity-Academy-Python-Scripting/
│
├── sql-injection/
├── xss/
├── csrf/
├── command-injection/
├── path-traversal/
├── file-upload/
├── ssrf/
├── jwt/
├── xxe/
│
├── common/
│   ├── helpers.py
│   ├── requests.py
│   └── utils.py
│
└── README.md
```

As the repository grows, each directory will contain multiple scripting examples covering different techniques and levels of complexity.

---

## Technologies

- Python 3
- requests
- BeautifulSoup
- urllib
- colorama
- Standard Python libraries

Additional libraries may be introduced where appropriate.

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/yourusername/WebSecurity-Academy-Python-Scripting.git

cd WebSecurity-Academy-Python-Scripting
```

Install the required dependencies:

```bash
python3 -m pip install requests beautifulsoup4 colorama
```

Each topic directory contains one or more Python scripts demonstrating a specific web security technique or automation approach.

---

## Disclaimer

The material in this repository is provided for educational purposes only.

All scripts are intended to be used exclusively against deliberately vulnerable applications, laboratory environments, or systems for which you have obtained explicit authorisation.

The author accepts no responsibility for misuse of the information or code contained within this repository.

---

## Acknowledgements

A special thanks to **PortSwigger** for creating the excellent **Web Security Academy**, which provides one of the best free platforms for learning web application security through hands-on labs.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
