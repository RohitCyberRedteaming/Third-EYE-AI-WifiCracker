import pandas as pd
import subprocess
import os
import time
from tabulate import tabulate
from colorama import Fore

def wifi_scan(interface):
    """
    Scans for nearby networks using airodump-ng and formats 
    results for Auto-Selection in ThirdEye v1.1.
    """
    print(Fore.BLUE + "\n[*] Scanning for 15 seconds... (Press Ctrl+C to stop early)")
    
    # Remove old scan files to prevent data mixing
    # 'thirdeye_scan' prefix ensures we don't delete other CSVs
    os.system("rm -f thirdeye_scan-01.csv")
    
    # Command to run airodump-ng
    cmd = ["sudo", "airodump-ng", "--write", "thirdeye_scan", "--output-format", "csv", interface]
    
    # Running the process in background
    proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    try:
        # Scan duration
        time.sleep(15)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[*] Scan stopped early by user.")
        pass
    
    # Stopping the scan process
    proc.terminate()
    
    file_path = "thirdeye_scan-01.csv"
    if os.path.exists(file_path):
        try:
            # Read CSV and drop rows without BSSID (headers/clients)
            df = pd.read_csv(file_path, skipinitialspace=True).dropna(subset=['BSSID'])
            
            # CRITICAL: Reset index to 0, 1, 2... for clean Auto-Selection
            df = df.reset_index(drop=True)
            
            # Displaying the clean target list
            print(Fore.GREEN + "\n--- TARGET LIST ---")
            # showindex=True adds the 0, 1, 2 column for user to pick
            print(tabulate(df[['BSSID', 'channel', 'pwr', 'essid']], 
                           headers=['ID', 'BSSID', 'CH', 'PWR', 'ESSID'], 
                           tablefmt='psql', 
                           showindex=True))
            
            return df
        except Exception as e:
            print(Fore.RED + f"[!] Parsing Error: {e}")
    else:
        print(Fore.RED + "[!] Error: thirdeye_scan-01.csv not found. Check monitor mode.")
        
    return None
