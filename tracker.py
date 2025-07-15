import requests
import sys

def get_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'success':
        print("\n[+] IP Information Found:")
        print(f"IP: {data['query']}")
        print(f"Country: {data['country']}")
        print(f"Region: {data['regionName']}")
        print(f"City: {data['city']}")
        print(f"ISP: {data['isp']}")
        print(f"Lat: {data['lat']}")
        print(f"Lon: {data['lon']}")
    else:
        print("[-] IP Not Found or API Limit Reached")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tracker.py <ip_address>")
    else:
        ip = sys.argv[1]
        get_info(ip)
