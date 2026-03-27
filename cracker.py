import subprocess
import os
from colorama import Fore

class ThirdEyeCracker:
    def __init__(self):
        # Default wordlist path for Kali Linux
        self.default_wordlist = "/usr/share/wordlists/rockyou.txt"

    def crack_wpa(self, cap_file, wordlist=None):
        """Uses aircrack-ng to crack the WPA handshake."""
        if not wordlist:
            wordlist = self.default_wordlist

        if not os.path.exists(cap_file):
            print(Fore.RED + f"[!] Error: Capture file '{cap_file}' not found.")
            return

        if not os.path.exists(wordlist):
            print(Fore.RED + f"[!] Error: Wordlist '{wordlist}' not found. Please provide a valid path.")
            return

        print(Fore.CYAN + f"[*] Starting Cracking Engine on {cap_file}...")
        print(Fore.YELLOW + f"[*] Using Wordlist: {wordlist}")

        # Running aircrack-ng command
        cmd = ["sudo", "aircrack-ng", "-w", wordlist, cap_file]
        
        try:
            # This will show the cracking progress in the terminal
            subprocess.run(cmd)
        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] Cracking session interrupted by user.")

    def update_wordlist_api(self):
        """
        AI-Ready Logic: Fetches the latest common passwords from an Open API.
        (Placeholder for the API integration we discussed)
        """
        print(Fore.BLUE + "[*] Connecting to Open-Source Password API for updates...")
        # Add logic here to download 'rockyou' or other updated lists
