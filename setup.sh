#!/bin/bash
# ThirdEye v1.1 Unified Setup Script (Linux & Termux)

echo -e "\e[1;34m🧿 ThirdEye: Initializing Advanced Setup...\e[0m"

# 1. Environment Detection
if [ -d "/data/data/com.termux" ]; then
    ENV="Termux"
    INSTALL_CMD="pkg install -y"
    PYTHON_CMD="python"
else
    ENV="Linux"
    INSTALL_CMD="sudo apt update && sudo apt install -y"
    PYTHON_CMD="python3"
fi
echo -e "\e[1;32m[*] Detected Environment: $ENV\e[0m"

# 2. Dependency Installation
echo -e "\e[1;33m[*] Installing Core Dependencies (Aircrack, Hashcat, hcxtools)...\e[0m"
$INSTALL_CMD aircrack-ng reaver pixiewps hashcat hcxtools python nmap curl wget

# 3. GUI Dependency (Linux Only)
if [ "$ENV" == "Linux" ]; then
    echo -e "\e[1;33m[*] Installing GUI Components (Tkinter)...\e[0m"
    sudo apt install -y python3-tk
fi

# 4. Python Libraries
echo -e "\e[1;33m[*] Installing Python Libraries (Pandas, Tabulate, Colorama)...\e[0m"
pip install pandas tabulate colorama

# 5. Wordlist Setup (Smart Logic)
if [ ! -f "rockyou.txt" ]; then
    # Linux standard path check
    LINUX_ROCKYOU="/usr/share/wordlists/rockyou.txt"
    if [ -f "$LINUX_ROCKYOU" ]; then
        echo -e "\e[1;32m[✓] Found Rockyou in Linux standard path. Linking...\e[0m"
        ln -s "$LINUX_ROCKYOU" "rockyou.txt"
    else
        echo -e "\e[1;33m[*] Wordlist not found. Downloading (Fast Download)...\e[0m"
        # Downloading compressed version to save data
        curl -L -o rockyou.txt.gz https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt.gz
        echo -e "\e[1;32m[*] Extracting rockyou.txt...\e[0m"
        gunzip rockyou.txt.gz
        echo -e "\e[1;32m[✓] Wordlist Ready!\e[0m"
    fi
else
    echo -e "\e[1;32m[✓] rockyou.txt already exists.\e[0m"
fi

# 6. File Integrity Check
FILES=("main.py" "gui_main.py" "scanner.py" "attacks.py" "cracker.py" "utils.py")
for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "\e[1;32m[✓] $file found.\e[0m"
        chmod +x "$file"
    else
        echo -e "\e[1;31m[!] Warning: $file is missing!\e[0m"
    fi
done

# 7. Final Instructions
echo -e "\e[1;36m\n[+] Setup Complete! ThirdEye v1.1 is ready.\e[0m"
echo -e "------------------------------------------------"
if [ "$ENV" == "Linux" ]; then
    echo -e "Linux (GUI): sudo $PYTHON_CMD gui_main.py"
    echo -e "Linux (CLI): sudo $PYTHON_CMD main.py"
else
    echo -e "Termux (CLI): tsu -c '$PYTHON_CMD main.py'"
fi
echo -e "------------------------------------------------"
