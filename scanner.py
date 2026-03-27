import pandas as pd
import subprocess
import os
import time
from tabulate import tabulate
from colorama import Fore

def wifi_scan(interface):
    """Scans for nearby networks using airodump-ng."""
    print(Fore.BLUE + "[*] Scanning for 15 seconds... (Press Ctrl+C to stop early)")
    
    # Remove old scan files to prevent data mixing
    os.system("rm -f thirdeye_scan-01.csv")
    
    cmd = ["sudo", "airodump-ng", "--write", "thirdeye_scan", "--output-format", "csv", interface]
    proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    try:
        time.sleep(15)
    except KeyboardInterrupt:
        pass
    
    proc.terminate()
    
    file_path = "thirdeye_scan-01.csv"
    if os.path.exists(file_path):
        try:
            df = pd.read_csv(file_path, skipinitialspace=True).dropna(subset=['BSSID'])
            # Clean display columns
            print(Fore.GREEN + "\n--- TARGET LIST ---")
            print(tabulate(df[['BSSID', 'channel', 'pwr', 'essid']], headers='keys', tablefmt='psql'))
            return df
        except Exception as e:
            print(Fore.RED + f"[!] Parsing Error: {e}")
    return None
