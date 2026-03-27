import subprocess
import os
from colorama import Fore, Style

class ThirdEyeCracker:
    def __init__(self):
        # Default wordlist for Kali Linux
        self.default_wordlist = "/usr/share/wordlists/rockyou.txt"

    def crack_with_hashcat(self, cap_file, wordlist=None):
        """
        ADVANCED: Uses Hashcat (GPU Power) - 10x Faster.
        Requires 'hcxtools' to convert .cap to .hc22000 format.
        """
        if not wordlist: wordlist = self.default_wordlist
        
        # Hashcat conversion
        hash_file = cap_file.replace(".cap", ".hc22000")
        
        print(Fore.MAGENTA + Style.BRIGHT + "[*] AI-Optimizing: Converting .cap to Hashcat format...")
        
        # Converting .cap to .hc22000 using hcxpcapngtool
        convert_cmd = ["hcxpcapngtool", "-o", hash_file, cap_file]
        subprocess.run(convert_cmd, capture_output=True)

        if os.path.exists(hash_file):
            print(Fore.GREEN + "[+] Conversion Successful! Launching GPU Engine...")
            # -m 22000 is for WPA-PBKDF2-PMKID+EAPOL
            # --force is used to bypass virtual machine warnings
            cmd = ["hashcat", "-m", "22000", hash_file, wordlist, "--force"]
            try:
                subprocess.run(cmd)
            except Exception as e:
                print(Fore.RED + f"[!] Hashcat Error: {e}")
        else:
            print(Fore.RED + "[!] Conversion Failed. Ensure 'hcxtools' is installed via setup.sh")

    def crack_wpa_standard(self, cap_file, wordlist=None):
        """
        STANDARD: Uses Aircrack-ng (CPU Power).
        Reliable but slower than Hashcat.
        """
        if not wordlist: wordlist = self.default_wordlist
        
        print(Fore.CYAN + "[*] Launching Standard CPU Engine (Aircrack-ng)...")
        cmd = ["sudo", "aircrack-ng", "-w", wordlist, cap_file]
        
        try:
            subprocess.run(cmd)
        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] Cracking session stopped by user.")

    def auto_crack_selector(self, cap_file, wordlist=None):
        """
        AI Logic: Automatically chooses the best method based on available hardware.
        """
        print(Fore.WHITE + "\n--- Select Cracking Engine ---")
        print("1. Hashcat (GPU - Ultra Fast)")
        print("2. Aircrack-ng (CPU - Standard)")
        
        choice = input(Fore.YELLOW + "Choose (1/2): ")
        if choice == '1':
            self.crack_with_hashcat(cap_file, wordlist)
        else:
            self.crack_wpa_standard(cap_file, wordlist)
