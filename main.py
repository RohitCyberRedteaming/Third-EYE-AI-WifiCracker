import os
import pandas as pd
from colorama import Fore, Style, init
from utils import check_root, toggle_monitor, create_folders
from scanner import wifi_scan
from attacks import ThirdEyeAttacks
from cracker import ThirdEyeCracker

# Initialize Colorama for colors
init(autoreset=True)

# Global variable to store last scan results
last_scan_results = None

def banner():
    """Displays the ThirdEye branding."""
    os.system('clear' if os.name != 'nt' else 'cls')
    print(Fore.CYAN + Style.BRIGHT + r"""
    #######################################################
    #            THIRD-EYE WIFI-CRACKER v1.1              #
    #        [ Unified Linux & Termux - AutoSelect ]      #
    #######################################################
    """)

def select_target():
    """Helper function to pick a target from the last scan."""
    global last_scan_results
    if last_scan_results is None or last_scan_results.empty:
        print(Fore.RED + "[!] No scan data found. Please run a Scan (Option 1) first.")
        return None, None, None

    try:
        idx = int(input(Fore.YELLOW + "\nEnter Target Number (e.g., 0, 1, 2): "))
        target = last_scan_results.iloc[idx]
        bssid = target['BSSID']
        channel = str(target['channel'])
        essid = target['essid']
        print(Fore.GREEN + f"[+] Selected: {essid} ({bssid}) on Channel {channel}")
        return bssid, channel, essid
    except (ValueError, IndexError):
        print(Fore.RED + "[!] Invalid selection. Check the list and try again.")
        return None, None, None

def main():
    global last_scan_results
    
    # 1. Environment Detection
    is_termux = os.path.exists("/data/data/com.termux")
    if not is_termux:
        check_root() # Only for Linux
    
    create_folders()
    banner()
    
    print(Fore.WHITE + f"[*] Mode: {Fore.YELLOW}{'Termux (Mobile)' if is_termux else 'Linux (PC)'}")
    
    iface = input(Fore.WHITE + "Enter Interface (e.g., wlan0): ")
    toggle_monitor(iface, "start")
    
    # Auto-handle monitor interface name
    mon_iface = iface + "mon" if not iface.endswith("mon") else iface
    
    attack_engine = ThirdEyeAttacks(mon_iface)
    cracker_engine = ThirdEyeCracker()
    
    while True:
        print(f"\n{Fore.CYAN}--- MAIN MENU ---")
        print(f"{Fore.GREEN}1. Scan Networks (Visibility Mode)")
        print(f"{Fore.GREEN}2. Capture Handshake (Auto-Select Target)")
        print(f"{Fore.GREEN}3. WPS Pixie-Dust (Auto-Select Target)")
        print(f"{Fore.GREEN}4. Crack Handshake (Hashcat/Aircrack-ng)")
        print(f"{Fore.GREEN}5. Exit & Cleanup")
        
        choice = input(Fore.YELLOW + "\nThirdEye > ")
        
        if choice == '1':
            # Scan returns a DataFrame
            last_scan_results = wifi_scan(mon_iface)
            if last_scan_results is not None:
                print(Fore.BLUE + "\n[*] Networks found. You can now use Option 2 or 3.")
            
        elif choice == '2':
            b, c, e = select_target()
            if b:
                attack_engine.handshake_capture(b, c, e)
            
        elif choice == '3':
            b, c, e = select_target()
            if b:
                attack_engine.wps_pixie(b)
            
        elif choice == '4':
            cap_path = input(Fore.WHITE + "Path to .cap file (e.g., captures/wifi-01.cap): ")
            cracker_engine.auto_crack_selector(cap_path)
            
        elif choice == '5':
            toggle_monitor(mon_iface, "stop")
            print(Fore.CYAN + "[+] Monitor mode disabled. Stay safe! Goodbye.")
            break
        
        else:
            print(Fore.RED + "[!] Invalid choice.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n[!] Interrupted by user. Cleaning up and exiting...")
