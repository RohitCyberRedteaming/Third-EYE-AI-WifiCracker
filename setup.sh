#!/bin/bash
echo "Setting up ThirdEye dependencies..."
sudo apt update
sudo apt install -y aircrack-ng reaver pixiewps bully tshark hcxtools python3-pandas python3-tabulate python3-colorama
echo "Done. Run 'sudo python3 main.py' to start."
