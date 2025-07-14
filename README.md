# MiniPortScanner 🔍

Lightweight Python 3 port scanner that runs everywhere (macOS, Linux, Windows) and requires **no external libraries** for the basic TCP connect scan.  
Built for learning, extensibility, and ethical use only.

<p align="center">
  <img src="https://raw.githubusercontent.com/<your-github-user>/port-scanner/main/assets/demo.gif" alt="Terminal demo" width="680">
</p>

---

## ✨ Features

- **MVP** – multithreaded TCP connect scan, CIDR-block targeting, human-readable output.
- Optional **UDP** and **Nmap parsing** (via `python-nmap`).
- Clear, well-commented code (≈150 LOC) for easy hacking.
- Runs on Python ≥ 3.10 (tested on macOS 14, Kali 2025.2, Windows 11).

---

## 🔧 Requirements

| Component | Version |
|-----------|---------|
| Python    | 3.10 – 3.13 |
| Git       | any recent |
| Nmap      | *(optional)* for comparison / advanced scans |

Install the Python extras:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


🚀 Usage
bash
Copy
Edit
# Basic scan of three common ports on a single host
python scanner.py 192.168.1.10 -p 22,80,443

# Scan a whole /24 subnet, first 1024 ports
python scanner.py 192.168.1.0/24

# Pretty colors (requires colorama)
python scanner.py scanme.nmap.org -p 1-1024
Flag	Description	Default
target	IP, hostname, or CIDR block	n/a
-p, --ports	Comma list or range (1-65535)	1-1024

🗺️ Roadmap
Asyncio engine for ~10× speed on large scans.

Service banner grab (recv) after open port detected.

JSON/CSV report for SIEM ingestion.

CI workflow (GitHub Actions on macOS & Ubuntu).

PyPI package + Homebrew tap installation.

🤝 Contributing

Fork the project & create your branch: git checkout -b feature/foo.

Commit changes: git commit -m 'Add foo'.

Push to the branch: git push origin feature/foo.

Open a pull request.