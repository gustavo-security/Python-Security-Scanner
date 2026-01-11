import requests

SENSITIVE_PATHS = [
    "/tasks",
    "/tasks/search",
    "/tasks/1"
]

def check_auth(base_url):
    vulnerable = []
    
    for path in SENSITIVE_PATHS:
        try:
            response = requests.get(f"{base_url}{path}", timeout=5)

            if response.status_code not in [401, 403]:
                vulnerable.append(f"{path} → status {response.status_code}")

        except Exception as e:
            vulnerable.append(f"{path} → error: {str(e)}")

    if vulnerable:
        return {
            "check": "Authentication & Authorization",
            "status": "FAIL",
            "details": "Possibly unprotected endpoints:\n" + "\n".join(vulnerable)
        }

    return {
        "check": "Authentication & Authorization",
        "status": "OK",
        "details": "All sensitive endpoints are protected (401/403 without token)."
    }