# 📄 README.md (Official ThirdEye Manual)

```markdown
# 🧿 ThirdEye Wifi-Cracker v1.1
> **The Ultimate Unified Wireless Security Auditing Suite for Linux & Android (Termux)**

ThirdEye ek advanced pentesting tool hai jo security professionals aur ethical hackers ke liye banaya gaya hai. Ye tool automatically WiFi networks ko scan karta hai, handshake capture karta hai, aur multiple engines (GPU/CPU) ka use karke password crack karta hai.

---

## ⚖️ LEGAL DISCLAIMER
**WARNING:** Is tool ka upyog sirf authorized security auditing aur educational purposes ke liye karein. Bina permission kisi ke wireless network par attack karna **Gair-kanooni (Illegal)** hai. Developer kisi bhi tarah ke misuse ya nuksaan ke liye zimmedar nahi hoga. 

---

## 📱 Platforms Supported
1. **Linux:** Kali Linux, Parrot OS, Ubuntu (Full GPU/CPU Support).
2. **Android:** Termux (Requires Root + External WiFi Adapter).

---

## 🛠️ Quick Installation

Sabse pehle repository ko clone karein aur automatic setup script run karein:

```bash
git clone [https://github.com/YOUR_USERNAME/ThirdEye.git](https://github.com/YOUR_USERNAME/ThirdEye.git)
cd ThirdEye
bash setup.sh
```

### For Linux Users:
```bash
sudo python3 gui_main.py   # For Graphical Interface
# OR
sudo python3 main.py       # For Command Line Interface
```

### For Android (Termux) Users:
*Dhyan dein: Phone Rooted hona chahiye.*
```bash
tsu
python main.py
```

---

## 🚀 How To Use (Professional Manual)

ThirdEye v1.1 mein **Auto-Selection** feature hai, jisse typing ki galti nahi hoti. Niche diye gaye steps follow karein:

### Step 1: Scan (Intelligent Visibility)
Main menu mein **Option 1** select karein. Tool 15 seconds tak aas-paas ke sabhi WiFi networks ko scan karega aur unhe ek numbered list (0, 1, 2...) mein dikhayega.

### Step 2: Target Selection
Ab **Option 2** (Handshake) ya **Option 3** (Pixie-Dust) select karein. Tool aapse BSSID nahi puchega, balki kahega: `Enter Target Number`. Aap scan list se apne target ka number (index) type kar dein.

### Step 3: Attack & Capture
Tool automatically Deauthentication packets bhejega aur WPA/WPA2 Handshake capture karke use `captures/` folder mein save kar dega.

### Step 4: Cracking (Dual Engine)
**Option 4** select karein aur capture file ka path dein. 
- **Hashcat (Option 1):** Agar aap PC par hain aur fast cracking chahte hain.
- **Aircrack-ng (Option 2):** Agar aap Termux/Mobile par hain.

---

## 📂 Project Structure
- `main.py`: Unified CLI Controller (Best for Termux).
- `gui_main.py`: Professional Dashboard (Best for Linux).
- `setup.sh`: One-click dependency installer.
- `cracker.py`: Password cracking logic (GPU/CPU).
- `scanner.py`: Network discovery engine.
- `attacks.py`: Deauth & Pixie-Dust exploit module.
- `utils.py`: Monitor mode & system helpers.

---

## 🤝 Contribution & Support
Agar aapko koi bug milta hai ya aap koi feature add karna chahte hain, toh Pull Request open karein. 

**Developed with ❤️ for the Security Community.**
```

---

### 💡 GitHub par "Push" kaise karein?
Agar aap chahte hain ki ye project aapke GitHub par dikhe, toh terminal mein ye commands chalayein:

1. `git init`
2. `git add .`
3. `git commit -m "ThirdEye v1.1 Unified Release"`
4. `git branch -M main`
5. `git remote add origin https://github.com/YOUR_USERNAME/ThirdEye.git`
6. `git push -u origin main`
