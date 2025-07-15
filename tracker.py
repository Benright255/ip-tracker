import requests
import sys
import pyfiglet

def banner():
    ascii_banner = pyfiglet.figlet_format("IP Tracker")
    print(ascii_banner)
    print("===================================")
    print(" Author   : Benright255")
    print(" GitHub   : https://github.com/Benright255/ip-tracker")
    print("===================================\n")

def get_info(ip):
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

if __name__ == "__main__":
    banner()
    if len(sys.argv) != 2:
        print("Usage: python tracker.py <ip_address>")
    else:
        ip = sys.argv[1]
        get_info(ip)
