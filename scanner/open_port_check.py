import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL"
}


def check_open_ports(host):
    open_ports = []

    for port, service in COMMON_PORTS.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((host, port))
        sock.close()

        if result == 0:
            open_ports.append(f"{port} ({service})")

    if not open_ports:
        return {
            "check": "Open Ports",
            "status": "OK",
            "details": "No common ports are open."
        }
    else:
        return {
            "check": "Open Ports",
            "status": "WARNING",
            "details": f"Open ports detected: {', '.join(open_ports)}"
        }