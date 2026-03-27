# 🧿 ThirdEye Wifi-Cracker v1.0

**ThirdEye Wifi-Cracker** is a professional-grade, modular Wi-Fi Penetration Testing Suite designed for security researchers and ethical hackers. It automates complex tasks like handshake capturing, WPS Pixie-Dust attacks, and PMKID retrieval.

## 🚀 Features
- **Auto-Monitor Mode:** Automatically toggles wireless interfaces.
- **Intelligent Scanning:** Real-time target analysis using `airodump-ng`.
- **Attack Suite:** - WPA/WPA2 Handshake Capture (Deauth Attack)
    - WPS Pixie-Dust (Reaver Integration)
    - PMKID Client-less Capture
- **Built-in Cracker:** Dictionary-based cracking for `.cap` files.

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_USERNAME/ThirdEye-Wifi-Cracker.git](https://github.com/YOUR_USERNAME/ThirdEye-AI-WifiCracker.git)
cd ThirdEye-Wifi-Cracker

2- Run Setup Script
chmod +x setup.sh
sudo ./setup.sh

3- Launch Tool
sudo python3 main.py

📱 Platforms Supported
Kali Linux (Recommended)

Parrot Security OS

Termux (Rooted + External Wireless Adapter)

⚠️ Disclaimer
Usage of ThirdEye Wifi-Cracker for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

---

### 2. GitHub par Upload karne ka Tarika (Terminal se)

Agar aapne GitHub par naya repository bana liya hai, toh apne VS Code terminal mein ye commands chalayein:

1.  **Git Initialize karein:**
    `git init`
2.  **Files Add karein:**
    `git add .`
3.  **Commit karein:**
    `git commit -m "Initial commit - ThirdEye v1.0 Ready"`
4.  **Branch Set karein:**
    `git branch -M main`
5.  **Remote Repository link karein:** (Apna URL yahan dalein)
    `git remote add origin https://github.com/YOUR_USERNAME/ThirdEye-Wifi-Cracker.git`
6.  **Push karein:**
    `git push -u origin main`

---

### 3. .gitignore File (Important)
GitHub par faltu files (jaise scan results ya captured passwords) upload nahi honi chahiye. Ek `.gitignore` file banayein aur usme ye likhein:
```text
*.csv
*.cap
*.netxml
__pycache__/
captures/
scan*
