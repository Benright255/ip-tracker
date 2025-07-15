import requests
import sys
import pyfiglet
import phonenumbers
from phonenumbers import geocoder, carrier, number_type
import os

def banner():
    ascii_banner = pyfiglet.figlet_format("TRACKER")
    print(ascii_banner)
    print("===================================")
    print(" Author   : Benright255")
    print(" GitHub   : https://github.com/Benright255/ip-tracker")
    print("===================================\n")

def auto_update():
    print("\n[+] Checking for updates from GitHub...")
    os.system("git pull")
    print("[+] Update check complete!\n")

def ip_tracker(ip):
    url = f"http://ip-api.com/json/{ip}?fields=status,message,query,reverse,country,regionName,city,zip,lat,lon,isp,org,as,timezone"
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'success':
        print("[+] IP Information Found:\n")
        print(f"IP Address : {data['query']}")
        print(f"Reverse DNS: {data.get('reverse', 'N/A')}")
        print(f"Country    : {data['country']}")
        print(f"Region     : {data['regionName']}")
        print(f"City       : {data['city']} ({data['zip']})")
        print(f"Timezone   : {data['timezone']}")
        print(f"ISP        : {data['isp']}")
        print(f"Organization: {data['org']}")
        print(f"AS Number  : {data['as']}")
        print(f"Latitude   : {data['lat']}")
        print(f"Longitude  : {data['lon']}")
        print(f"Google Maps: https://www.google.com/maps/search/?api=1&query={data['lat']},{data['lon']}")
    else:
        print("[-] IP Not Found or Error:", data.get('message', 'Unknown Error'))

def phone_tracker(phone):
    try:
        parsed_number = phonenumbers.parse(phone, None)
        print("[+] Phone Number Information:\n")
        print(f"Number      : {phone}")
        print(f"Country     : {geocoder.description_for_number(parsed_number, 'en')}")
        print(f"Carrier     : {carrier.name_for_number(parsed_number, 'en')}")
        print(f"Number Type : {number_type(parsed_number)}")
        print(f"Region Code : {parsed_number.country_code}")
    except:
        print("[-] Invalid phone number format. Use international format e.g +255XXXXXXXXX")

if __name__ == "__main__":
    banner()
    auto_update()
    if len(sys.argv) != 2:
        print("Usage: python tracker.py <ip_address | phone_number>")
    else:
        target = sys.argv[1]
        if target.replace(".", "").isdigit():
            ip_tracker(target)
        elif target.startswith("+") and target[1:].isdigit():
            phone_tracker(target)
        else:
            print("[-] Invalid input. Enter a valid IP or phone number starting with +")
