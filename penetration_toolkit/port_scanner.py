import socket

def port_scanner(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is open")
            sock.close()
        except Exception as e:
            print(f"[-] Error scanning port {port}: {e}")

if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]
    port_scanner(target, ports)
