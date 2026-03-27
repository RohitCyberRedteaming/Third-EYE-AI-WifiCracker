import subprocess
import os
from colorama import Fore, Style

class ThirdEyeCracker:
    def __init__(self):
        # Detect environment
        self.is_termux = os.path.exists("/data/data/com.termux")
        
        # Smart Wordlist Detection
        # Linux standard path vs Termux local path
        linux_rockyou = "/usr/share/wordlists/rockyou.txt"
        termux_rockyou = "rockyou.txt" # setup.sh downloads it here

        if not self.is_termux and os.path.exists(linux_rockyou):
            self.default_wordlist = linux_rockyou
        elif os.path.exists(termux_rockyou):
            self.default_wordlist = termux_rockyou
        else:
            # Fallback if not found
            self.default_wordlist = "rockyou.txt"

    def run_cmd(self, cmd_list):
        """Helper to handle sudo based on platform."""
        if not self.is_termux:
            if cmd_list[0] != "sudo":
                cmd_list.insert(0, "sudo")
        return cmd_list

    def crack_with_hashcat(self, cap_file, wordlist=None):
        """
        ADVANCED: Uses Hashcat (GPU Power).
        Note: Hashcat is mostly used on Linux PC.
        """
        if self.is_termux:
            print(Fore.RED + "[!] Warning: Hashcat is heavy for mobile. Aircrack-ng is recommended for Termux.")
            
        if not wordlist: wordlist = self.default_wordlist
        
        # Check if wordlist exists
        if not os.path.exists(wordlist):
            print(Fore.RED + f"[!] Error: Wordlist not found at {wordlist}")
            return

        hash_file = cap_file.replace(".cap", ".hc22000")
        print(Fore.MAGENTA + Style.BRIGHT + "[*] AI-Optimizing: Converting .cap to Hashcat format...")
        
        # Convert command
        convert_cmd = self.run_cmd(["hcxpcapngtool", "-o", hash_file, cap_file])
        subprocess.run(convert_cmd, capture_output=True)

        if os.path.exists(hash_file):
            print(Fore.GREEN + "[+] Conversion Successful! Launching GPU Engine...")
            # -m 22000 for WPA2
            cmd = self.run_cmd(["hashcat", "-m", "22000", hash_file, wordlist, "--force"])
            try:
                subprocess.run(cmd)
            except Exception as e:
                print(Fore.RED + f"[!] Hashcat Error: {e}")
        else:
            print(Fore.RED + "[!] Conversion Failed. Ensure 'hcxtools' is installed.")

    def crack_wpa_standard(self, cap_file, wordlist=None):
        """
        STANDARD: Uses Aircrack-ng (CPU Power).
        Best for Termux and low-end Linux systems.
        """
        if not wordlist: wordlist = self.default_wordlist
        
        if not os.path.exists(wordlist):
            print(Fore.RED + f"[!] Error: Wordlist not found at {wordlist}")
            return

        print(Fore.CYAN + f"[*] Launching CPU Engine (Aircrack-ng) using {wordlist}...")
        cmd = self.run_cmd(["aircrack-ng", "-w", wordlist, cap_file])
        
        try:
            subprocess.run(cmd)
        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] Cracking session stopped by user.")

    def auto_crack_selector(self, cap_file):
        """
        User chooses the engine. Default wordlist is auto-detected.
        """
        if not os.path.exists(cap_file):
            print(Fore.RED + f"[!] Error: File '{cap_file}' not found!")
            return

        print(Fore.WHITE + "\n--- Select Cracking Engine ---")
        print(Fore.GREEN + "1. Hashcat (Best for Linux PC with GPU)")
        print(Fore.GREEN + "2. Aircrack-ng (Best for Termux/Mobile)")
        
        choice = input(Fore.YELLOW + "Choose (1/2): ")
        
        # Ask for custom wordlist or use default
        custom_word = input(Fore.WHITE + f"Wordlist path (Enter for {self.default_wordlist}): ")
        final_word = custom_word if custom_word.strip() != "" else self.default_wordlist

        if choice == '1':
            self.crack_with_hashcat(cap_file, final_word)
        else:
            self.crack_wpa_standard(cap_file, final_word)
