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
===================================================================================================================================================================
===================================================================================================================================================================
📱 2. Mobile APK / Termux Process (Step-by-Step)
Android par ise chalane ke liye koi .apk file nahi banti, balki Termux ka use hota hai. Kyunki ye tool hardware access karta hai, aapka phone ROOTED hona chahiye aur aapke paas ek External WiFi Adapter (jo monitor mode support kare) hona chahiye.

Step 1: Install Termux
Play Store wala Termux purana hai, F-Droid website se latest Termux download karein.

Step 2: Setup Root Environment
Termux open karein aur ye commands dalein:

Bash
pkg update && pkg upgrade -y
pkg install tsu python git -y
Step 3: Setup Dependencies (Termux specific)
Kyunki Termux mein apt ki jagah pkg hota hai, aapka setup.sh thoda alag hoga:

Bash
pkg install aircrack-ng reaver pixiewps bully tshark -y
pip install pandas tabulate colorama
Step 4: Connect WiFi Adapter
Apne external WiFi card ko OTG cable se connect karein. Termux mein type karein:

Bash
lsusb
Agar aapka card list mein dikh raha hai, toh aap ready hain.

Step 5: Run ThirdEye
Bash
tsu  # Root access switch karein
python main.py
