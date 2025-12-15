"""
Port Scanner Tool
-----------------

What is this tool?
    A lightweight Python-based port scanner designed for security learners and 
    analysts. It performs simple TCP connection attempts to identify which 
    ports are open on a target system.

What does this tool do?
    - Scans a list of predefined common ports (from common_ports.py)
    - Attempts TCP socket connections to each port
    - Reports which ports are open or closed
    - Provides optional service names for easier interpretation

How does this streamline actions?
    Instead of manually checking ports one-by-one with commands like:
        nc -zv target port
        telnet target port
        nmap (full scan)
    This script automates that workflow by scanning multiple ports quickly 
    and summarizing the results in a clean, readable format.

How to use it (best practices):
    - Run the script from the command line:
        python3 scanner.py <target-ip>

    - Make sure the target is a system you have permission to scan
    - Use fast scans for internal testing; use advanced scanning tools (like Nmap)
      for full security assessments

Example:
    python3 scanner.py 192.168.1.1

Output Meaning:
    OPEN   — The scanner successfully connected to the port  
    CLOSED — The connection was refused or timed out  
    SERVICE — (Optional) A label explaining what the port is commonly used for

    Example output:
        22/tcp  OPEN   SSH
        80/tcp  OPEN   HTTP
        443/tcp CLOSED HTTPS

This output gives you a quick picture of what services might be running on the host.
"""


import socket

def scan_port(target, port):
    """Attempts to connect to a single port."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0  # True = open, False = closed
    except:
        return False

def main():
    target = input("Enter target IP or hostname: ")

    print(f"\nScanning {target}...\n")

    # List of common ports (we will load this from common_ports.py later)
    common_ports = [22, 80, 443]

    for port in common_ports:
        if scan_port(target, port):
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is closed")

    print("\nScan complete.")

if __name__ == "__main__":
    main()

