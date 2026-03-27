import os
from colorama import Fore, Style, init
from utils import check_root, toggle_monitor
from scanner import wifi_scan
from attacks import ThirdEyeAttacks

init(autoreset=True)

def banner():
    os.system('clear')
    print(Fore.CYAN + Style.BRIGHT + r"""
    #######################################################
    #            THIRD-EYE WIFI-CRACKER v1.0              #
    #        Authorized Security Auditing Suite           #
    #######################################################
    """)

def main():
    check_root()
    banner()
    
    iface = input(Fore.WHITE + "Enter Wireless Interface (e.g., wlan0): ")
    toggle_monitor(iface, "start")
    
    # Update interface name for monitor mode (airmon-ng usually adds 'mon')
    mon_iface = iface + "mon" if not iface.endswith("mon") else iface
    attack_engine = ThirdEyeAttacks(mon_iface)
    
    while True:
        print(f"\n{Fore.GREEN}1. Scan Networks")
        print(f"{Fore.GREEN}2. Capture WPA Handshake")
        print(f"{Fore.GREEN}3. WPS Pixie-Dust Attack")
        print(f"{Fore.GREEN}4. Exit & Stop Monitor Mode")
        
        choice = input(Fore.YELLOW + "\nThirdEye > ")
        
        if choice == '1':
            wifi_scan(mon_iface)
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
