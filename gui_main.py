import tkinter as tk
from tkinter import ttk, messagebox
import threading
import os
from scanner import wifi_scan
from utils import toggle_monitor, check_root

class ThirdEyeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🧿 ThirdEye Wifi-Cracker v1.1")
        self.root.geometry("800x600")
        self.root.configure(bg="#121212")

        # Header
        tk.Label(root, text="THIRD-EYE PENTESTING GUI", font=("Courier", 20, "bold"), fg="#00ffcc", bg="#121212").pack(pady=10)

        # Control Frame
        ctrl_frame = tk.Frame(root, bg="#121212")
        ctrl_frame.pack(pady=5)

        tk.Label(ctrl_frame, text="Interface:", fg="white", bg="#121212").grid(row=0, column=0, padx=5)
        self.iface_entry = tk.Entry(ctrl_frame, width=10)
        self.iface_entry.insert(0, "wlan0")
        self.iface_entry.grid(row=0, column=1, padx=5)

        tk.Button(ctrl_frame, text="Enable Monitor Mode", command=self.enable_mon, bg="#007acc", fg="white").grid(row=0, column=2, padx=10)
        tk.Button(ctrl_frame, text="Scan Networks", command=self.start_scan_thread, bg="#28a745", fg="white").grid(row=0, column=3, padx=10)

        # Network Table (The Visibility Part)
        self.tree = ttk.Treeview(root, columns=("BSSID", "CH", "PWR", "ESSID"), show='headings', height=10)
        self.tree.heading("BSSID", text="BSSID")
        self.tree.heading("CH", text="CH")
        self.tree.heading("PWR", text="PWR")
        self.tree.heading("ESSID", text="ESSID")
        self.tree.column("CH", width=50, anchor="center")
        self.tree.column("PWR", width=50, anchor="center")
        self.tree.pack(pady=20, padx=20, fill=tk.X)

        # Console Output
        self.console = tk.Text(root, height=8, bg="#000", fg="#00ff00", font=("Courier", 10))
        self.console.pack(pady=10, padx=20, fill=tk.X)

    def log(self, msg):
        self.console.insert(tk.END, f"> {msg}\n")
        self.console.see(tk.END)

    def enable_mon(self):
        iface = self.iface_entry.get()
        self.log(f"Switching {iface} to monitor mode...")
        threading.Thread(target=lambda: toggle_monitor(iface, "start")).start()

    def start_scan_thread(self):
        self.log("Starting 15s scan... Table will update shortly.")
        threading.Thread(target=self.scan_and_update).start()

    def scan_and_update(self):
        iface = self.iface_entry.get()
        mon_iface = iface + "mon" if "mon" not in iface else iface
        df = wifi_scan(mon_iface)
        
        # Clear old data
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        # Insert new data
        if df is not None:
            for _, row in df.iterrows():
                self.tree.insert("", tk.END, values=(row['BSSID'], row['channel'], row['pwr'], row['essid']))
            self.log("Scan complete. Networks listed above.")
        else:
            self.log("Scan failed or no networks found.")

if __name__ == "__main__":
    root = tk.Tk()
    # check_root() # Un-comment this for real usage
    app = ThirdEyeGUI(root)
    root.mainloop()
