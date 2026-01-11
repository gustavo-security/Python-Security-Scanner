import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Referrer-Policy"
]


def check_security_headers(url):
    missing_headers = []

    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        for header in SECURITY_HEADERS:
            if header not in headers:
                missing_headers.append(header)

        if not missing_headers:
            return {
                "check": "Security Headers",
                "status": "OK",
                "details": "All recommended security headers are present."
            }
        else:
            return {
                "check": "Security Headers",
                "status": "WARNING",
                "details": f"Missing headers: {', '.join(missing_headers)}"
            }

    except requests.RequestException as e:
        return {
            "check": "Security Headers",
            "status": "ERROR",
            "details": f"Failed to connect to target: {str(e)}"
        }