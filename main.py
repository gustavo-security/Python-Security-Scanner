import sys
from urllib.parse import urlparse
from datetime import datetime

from scanner.headers_check import check_security_headers
from scanner.open_port_check import check_open_ports
from scanner.auth_check import check_auth


def generate_report(target_url, host, results):
    with open("reports/report.txt", "w") as file:
        file.write("========================================\n")
        file.write(" Python Security Scanner - Scan Report\n")
        file.write("========================================\n\n")

        file.write(f"Target URL: {target_url}\n")
        file.write(f"Host: {host}\n")
        file.write(f"Scan Date: {datetime.now()}\n\n")

        file.write("Checks executed:\n")
        file.write("- HTTP Security Headers\n")
        file.write("- Open Ports Scan\n")
        file.write("- Authentication & Authorization\n\n")

        file.write("========================================\n\n")

        for r in results:
            file.write(f"[{r['check']}]\n")
            file.write(f"Status: {r['status']}\n")
            file.write(f"Details: {r['details']}\n")
            file.write("-" * 40 + "\n")


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <url>")
        return

    target_url = sys.argv[1]

    parsed_url = urlparse(target_url)
    host = parsed_url.hostname

    results = []

    results.append(check_security_headers(target_url))
    results.append(check_open_ports(host))
    results.append(check_auth(target_url))

    generate_report(target_url, host, results)

    print("Scan completed. Report generated in reports/report.txt")


if __name__ == "__main__":
    main()