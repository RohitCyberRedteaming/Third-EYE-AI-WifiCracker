import os
from colorama import Fore, Style, init
from utils import check_root, toggle_monitor, create_folders
from scanner import wifi_scan
from attacks import ThirdEyeAttacks
from cracker import ThirdEyeCracker

init(autoreset=True)

def banner():
    os.system('clear')
    print(Fore.CYAN + Style.BRIGHT + r"""
    #######################################################
    #            THIRD-EYE WIFI-CRACKER v1.0              #
    #        [ AI-Managed Security Auditing Suite ]       #
    #######################################################
    """)

def main():
    check_root()      # Check for Sudo/Root
    create_folders()  # Auto-create 'captures/'
    banner()
    
    iface = input(Fore.WHITE + "Enter Wireless Interface (e.g., wlan0): ")
    toggle_monitor(iface, "start")
    
    mon_iface = iface + "mon" if not iface.endswith("mon") else iface
    attack_engine = ThirdEyeAttacks(mon_iface)
    cracker_engine = ThirdEyeCracker()
    
    while True:
        print(f"\n{Fore.GREEN}1. Scan Networks (Intelligent Scanner)")
        print(f"{Fore.GREEN}2. Capture WPA Handshake (Deauth Attack)")
        print(f"{Fore.GREEN}3. WPS Pixie-Dust (Vulnerability Exploit)")
        print(f"{Fore.GREEN}4. Crack Captured Handshake (Cracker Engine)")
        print(f"{Fore.GREEN}5. Exit & Stop Monitor Mode")
        
        choice = input(Fore.YELLOW + "\nThirdEye > ")
        
        if choice == '1':
            wifi_scan(mon_iface)
        elif choice == '2':
            b = input("Target BSSID: "); c = input("Channel: "); e = input("ESSID: ")
            attack_engine.handshake_capture(b, c, e)
        elif choice == '3':
            b = input("Target BSSID: ")
            attack_engine.wps_pixie(b)
        elif choice == '4':
            cap = input("Path to .cap file (e.g., captures/target-01.cap): ")
            word = input("Wordlist path (Press Enter for default /usr/share/wordlists/rockyou.txt): ")
            cracker_engine.crack_wpa(cap, word if word else None)
        elif choice == '5':
            toggle_monitor(mon_iface, "stop")
            print(Fore.CYAN + "[+] Cleanup complete. Goodbye!")
            break

if __name__ == "__main__":
    main()
        elif choice == '2':
            b = input("Target BSSID: ")
            c = input("Target Channel: ")
            e = input("Target ESSID: ")
            attack_engine.handshake_capture(b, c, e)
        elif choice == '3':
            b = input("Target BSSID: ")
            attack_engine.wps_pixie(b)
        elif choice == '4':
            toggle_monitor(mon_iface, "stop")
            print(Fore.YELLOW + "[+] Cleaning up... Goodbye!")
            break

if __name__ == "__main__":
    main()
