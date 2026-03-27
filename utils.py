import os
import subprocess
from colorama import Fore, Style

def check_root():
    """Ensures the script is running with sudo/root privileges."""
    if os.getuid() != 0:
        print(Fore.RED + Style.BRIGHT + "[!] Error: Root/Sudo privileges are required to access WiFi hardware.")
        exit()

def toggle_monitor(interface, mode="start"):
    """Toggles the WiFi card between Managed and Monitor mode."""
    print(Fore.YELLOW + f"[*] Switching {interface} to {mode} mode...")
    # 'check kill' stops interfering processes like NetworkManager
    if mode == "start":
        subprocess.run(["sudo", "airmon-ng", "check", "kill"], capture_output=True)
    subprocess.run(["sudo", "airmon-ng", mode, interface], capture_output=True)
