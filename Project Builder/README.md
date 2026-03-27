🛠️ ThirdEye v1.1: Master Builder GuideOne-Click Project Generator for Linux & Android (Termux)Ye build_v1.py script aapke liye pura ThirdEye WiFi-Cracker toolkit auto-generate kar degi. Aapko har file alag se copy-paste karne ki zaroorat nahi hai.📥 Installation Steps1. For Linux (Kali, Parrot, Ubuntu)Agar aap PC par hain, toh terminal kholein aur ye commands chalayein:Bash# 1. Builder run karein (Isse saari files generate ho jayengi)
python3 build_v1.py

# 2. Setup script ko permission dein aur run karein
chmod +x setup.sh
sudo ./setup.sh

# 3. Tool Launch karein
sudo python3 main.py
2. For Android (Termux - Root Required)Termux user hain toh tsu (root) ka hona zaroori hai:Bash# 1. Builder run karein
python build_v1.py

# 2. Setup run karein (Dependencies & Wordlist install karein)
bash setup.sh

# 3. Root access lein aur tool chalayein
tsu
python main.py
📂 Generated Files (Project Structure)Jab aap build_v1.py chalate hain, toh ye files banti hain:File NameDescriptionmain.pyMaster Menu: Auto-Select target feature ke saath.setup.shAuto-Installer: Dependencies aur rockyou.txt download karta hai.scanner.pyWiFi Scanner: Networks ko index (0, 1, 2...) mein dikhata hai.attacks.pyAttack Engine: Handshake capture aur Deauth attack handle karta.cracker.pyAI Cracker: GPU, CPU aur AI Guessing engine support.utils.pySystem Helper: Monitor mode aur Root check handle karta hai.ThirdEye_v1.1.zipPoore project ka compressed backup.🚀 How to Crack (Quick Start)Scan: Option 1 dabayein aur 15 seconds wait karein.Select: Option 2 dabayein aur scan list se Target ID (e.g., 0) enter karein.Capture: Tool khud Deauth bhej kar handshake pakad lega.Guess/Crack: Option 4 dabayein aur AI-Guessing chunein agar password common hone ka shaq ho.⚠️ Important NoteExternal Adapter: Termux users ko ek "Monitor Mode" support karne wala USB WiFi adapter (OTG ke saath) chahiye hoga.Wordlist: setup.sh automatically rockyou.txt download karega (133MB compressed).✅ Next Step for you:Maine builder aur installer sab ready kar diya hai. Kya aap chahte hain ki main gui_main.py (Visual Dashboard) ka poora updated code bhi is builder ke andar merge kar doon? Taaki ek hi click mein GUI file bhi generate ho jaye.
