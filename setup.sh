#!/bin/bash
# ThirdEye Unified Setup Script (GUI + CLI Edition)

echo -e "\e[1;34m🧿 ThirdEye: Initializing Advanced Setup...\e[0m"

# 1. Environment Detection
if [ -d "/data/data/com.termux" ]; then
    ENV="Termux"
    INSTALL_CMD="pkg install -y"
else
    ENV="Linux"
    INSTALL_CMD="sudo apt update && sudo apt install -y"
fi
echo -e "\e[1;32m[*] Detected Environment: $ENV\e[0m"

# 2. Dependency Installation
echo -e "\e[1;33m[*] Installing Core Dependencies...\e[0m"
$INSTALL_CMD aircrack-ng reaver pixiewps hashcat hcxtools python nmap curl

# 3. GUI Dependency (Linux Only)
if [ "$ENV" == "Linux" ]; then
    echo -e "\e[1;33m[*] Installing GUI Components (Tkinter)...\e[0m"
    sudo apt install -y python3-tk
fi

# 4. Python Libraries
pip install pandas tabulate colorama

# 5. File Integrity Check
FILES=("main.py" "gui_main.py" "scanner.py" "attacks.py" "cracker.py" "utils.py")
for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "\e[1;32m[✓] $file found.\e[0m"
    else
        echo -e "\e[1;31m[!] Warning: $file is missing! Some features may not work.\e[0m"
    fi
done

# 6. Wordlist Setup
if [ "$ENV" == "Termux" ] && [ ! -f "rockyou.txt" ]; then
    echo -e "\e[1;33m[*] Downloading Wordlist for Termux...\e[0m"
    curl -L -o rockyou.txt https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
fi

chmod +x main.py gui_main.py
echo -e "\e[1;36m\n[+] Setup Complete!\e[0m"
echo -e "Linux (GUI): sudo python3 gui_main.py"
echo -e "Linux (CLI): sudo python3 main.py"
echo -e "Termux: python main.py"
