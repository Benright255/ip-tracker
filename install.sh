#!/bin/bash

echo " "
echo "###############################################"
echo "         🌍 IP & Location Tracker 🔎"
echo "###############################################"
echo " Author   : Benright255"
echo " GitHub   : https://github.com/Benright255/ip-tracker"
echo "-----------------------------------------------"
echo " Installing Requirements..."
echo " "

pkg update -y && pkg upgrade -y
pkg install python -y
pip install requests

echo " "
echo "✅ Done Installing!"

echo " "
echo "To run the tool, use this command:"
echo " "
echo "    python tracker.py <ip_address>"
echo " "
echo "Example:"
echo "    python tracker.py 8.8.8.8"
echo " "
