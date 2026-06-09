import requests
import time
from concurrent.futures import ThreadPoolExecutor


MAX_RETRIES = 2


def check_server(url):

    start = time.perf_counter()

    response = None
    last_error = None

    for attempt in range(MAX_RETRIES):

        try:
            response = requests.get(url, timeout=5)

            # retry only for server/network issues
            if response.status_code < 500:
                break

        except requests.RequestException as e:
            last_error = e

            if attempt == MAX_RETRIES - 1:

                return {
                    "url": url,
                    "status_code": None,
                    "response_time": None,
                    "healthy": False,
                    "json_ok": False,
                    "slow": False,
                    "error": str(last_error)
                }

    elapsed = (time.perf_counter() - start) * 1000

    slow = elapsed > 500

    healthy = 200 <= response.status_code < 300

    json_ok = False

    try:
        data = response.json()
        if data.get("status") == "ok":
            json_ok = True
    except ValueError:
        pass

    return {
        "url": url,
        "status_code": response.status_code,
        "response_time": round(elapsed, 2),
        "healthy": healthy,
        "json_ok": json_ok,
        "slow": slow
    }


def check_all_servers(servers):

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(check_server, servers))

    return results