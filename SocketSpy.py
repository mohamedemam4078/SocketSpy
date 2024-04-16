import socket
from IPy import IP
import argparse

def scan(target, ports):
    print(f"\nScanning target: {target}")
    for port in range(1, ports + 1):
        scan_port(target, port)

def scan_port(ip_address, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ip_address, port))
        print(f"[+] Port {port} is open")
        sock.close()
    except:
        pass

def print_ascii_art():
    ascii_art = r"""

 _______  _______  _______  _        _______ _________    _______  _______          
(  ____ \(  ___  )(  ____ \| \    /\(  ____ \\__   __/   (  ____ \(  ____ )|\     /|
| (    \/| (   ) || (    \/|  \  / /| (    \/   ) (      | (    \/| (    )|( \   / )
| (_____ | |   | || |      |  (_/ / | (__       | |      | (_____ | (____)| \ (_) / 
(_____  )| |   | || |      |   _ (  |  __)      | |      (_____  )|  _____)  \   /  
      ) || |   | || |      |  ( \ \ | (         | |            ) || (         ) (   
/\____) || (___) || (____/\|  /  \ \| (____/\   | |    _ /\____) || )         | |   
\_______)(_______)(_______/|_/    \/(_______/   )_(   (_)\_______)|/          \_/   
                                                                                    

    """
    print(ascii_art)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Port Scanner')
    parser.add_argument('targets', metavar='TARGET', type=str, nargs='*', help='Target/s to scan (separate multiple targets with commas)')
    parser.add_argument('-p', '--ports', metavar='PORTS', type=int, default=1000, help='Number of ports to scan (default: 1000)')
    args = parser.parse_args()

    if args.targets:
        for target in args.targets:
            if '/' in target:
                for ip in IP(target):
                    scan(str(ip), args.ports)
            else:
                scan(target, args.ports)
    else:
        print_ascii_art()
        choice = input("\nEnter target/s to scan (separate multiple targets with commas): ").strip()
        targets = choice.split(',')
        ports = int(input("Enter number of ports to scan: "))
        for target in targets:
            if '/' in target:
                for ip in IP(target):
                    scan(str(ip), ports)
            else:
                scan(target, ports)
