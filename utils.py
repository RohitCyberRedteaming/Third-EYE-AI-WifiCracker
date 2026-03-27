import os
import subprocess
from colorama import Fore, Style

# Global check for environment
IS_TERMUX = os.path.exists("/data/data/com.termux")

def run_privileged(cmd_list):
    """
    Helper function to add 'sudo' only if NOT in Termux.
    """
    if not IS_TERMUX:
        if cmd_list[0] != "sudo":
            cmd_list.insert(0, "sudo")
    return cmd_list

def check_root():
    """Checks if the script has root privileges."""
    # In Termux, we check if the user has switched to 'tsu' or 'root'
    if os.getuid() != 0:
        if IS_TERMUX:
            print(Fore.RED + Style.BRIGHT + "[!] Access Denied: Please run 'tsu' before starting the script.")
        else:
            print(Fore.RED + Style.BRIGHT + "[!] Access Denied: Please run ThirdEye with 'sudo'.")
        exit()

def toggle_monitor(interface, mode="start"):
    """
    Switches the WiFi card between Managed and Monitor mode.
    Works on both Linux PC and Rooted Android (Termux).
    """
    try:
        print(Fore.YELLOW + f"[*] Setting {interface} to {mode} mode...")
        
        if mode == "start":
            # Kills background processes (interfering with monitor mode)
            kill_cmd = run_privileged(["airmon-ng", "check", "kill"])
            subprocess.run(kill_cmd, capture_output=True)
        
        # Enable/Disable monitor mode
        airmon_cmd = run_privileged(["airmon-ng", mode, interface])
        subprocess.run(airmon_cmd, capture_output=True)
        
        print(Fore.GREEN + f"[+] {interface} is now in {mode} mode.")
    except Exception as e:
        print(Fore.RED + f"[!] Error toggling monitor mode: {e}")

def create_folders():
    """Creates necessary folders for the project."""
    if not os.path.exists("captures"):
        os.makedirs("captures")
        print(Fore.CYAN + "[*] Project initialized: 'captures/' folder ready.")
