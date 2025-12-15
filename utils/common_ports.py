# common_ports.py

# A dictionary of common ports and their associated services
COMMON_PORTS = {
    20: "FTP (Data Transfer)",
    21: "FTP (Control)",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    143: "IMAP",
    161: "SNMP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    636: "LDAPS",
    3389: "RDP",
    8080: "HTTP Proxy"
}

# Returns a list of port numbers — used by scanner.py
def get_port_list():
    return list(COMMON_PORTS.keys())

