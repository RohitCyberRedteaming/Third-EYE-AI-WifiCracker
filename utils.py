import os
import subprocess
from colorama import Fore, Style

def check_root():
    """Checks if the script is running with root/sudo privileges."""
    if os.getuid() != 0:
        print(Fore.RED + Style.BRIGHT + "[!] Access Denied: Please run ThirdEye with 'sudo'.")
        exit()

def toggle_monitor(interface, mode="start"):
    """
    Switches the WiFi card between Managed and Monitor mode.
    Mode 'start' enables monitor mode, 'stop' disables it.
    """
    try:
        print(Fore.YELLOW + f"[*] Setting {interface} to {mode} mode...")
        if mode == "start":
            # Kills background processes that interfere with monitor mode
            subprocess.run(["sudo", "airmon-ng", "check", "kill"], capture_output=True)
        
        subprocess.run(["sudo", "airmon-ng", mode, interface], capture_output=True)
        print(Fore.GREEN + f"[+] {interface} is now in {mode} mode.")
    except Exception as e:
        print(Fore.RED + f"[!] Error toggling monitor mode: {e}")

def create_folders():
    """Creates necessary folders for the project if they don't exist."""
    if not os.path.exists("captures"):
        os.makedirs("captures")
        print(Fore.CYAN + "[*] Created 'captures/' folder for handshake storage.")
