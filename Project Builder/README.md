1. Linux (Kali, Parrot, ya Ubuntu) Par Kaise Chalayein
Linux par aapko full power milti hai (Monitor Mode + GPU Cracking).

Terminal Open Karein: Apne project folder mein jayein.

Setup Run Karein (Sirf ek baar):

Bash
bash setup.sh
(Ye saari dependencies aur Tkinter install kar dega)

GUI Mode Chalane Ke Liye (Visibility):

Bash
sudo python3 gui_main.py
Isme aapko buttons aur network table dikhegi.

CLI Mode Chalane Ke Liye (Terminal):

Bash
sudo python3 main.py
📱 2. Android (Termux) Par Kaise Chalayein
Termux par hacking ke liye aapka phone Rooted hona chahiye aur ek External WiFi Adapter OTG se juda hona chahiye.

Termux Open Karein: Aur project folder mein jayein (cd ThirdEye_V1.1).

Setup Run Karein (Sirf ek baar):

Bash
bash setup.sh
(Ye Termux ke liye rockyou.txt bhi download kar lega)

Root Access Lein:

Bash
tsu
Tool Launch Karein:

Bash
python main.py
Note: Termux mein GUI (gui_main.py) mat chalana, wo error dega kyunki Android mein native window support nahi hota.
