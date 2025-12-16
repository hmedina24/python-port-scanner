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
import ipaddress
from utils.common_ports import get_port_list

def resolve_target(target):
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        raise ValueError("Invalid hostname or IP Address")

def scan_port(target, port, timeout=0.5):
    if not isinstance(port, int) or port < 1 or port > 65535:
        raise ValueError("Port must be between 1 and 65535")

    target_ip = resolve_target(target)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    """Attempts to connect to a single port."""
    try:
        result = sock.connect_ex((target_ip, port))
        return result == 0 and "open" or "closed"
    finally:
        sock.close()

def main():
    target = input("Enter target IP or hostname: ")

    print(f"\nScanning {target}...\n")

    # List of common ports (we will load this from common_ports.py later)
    common_ports = get_port_list()

    for port in common_ports:
        status = scan_port(target, port)
        if status == "open":
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is closed")

    print("\nScan complete.")

if __name__ == "__main__":
    main()

