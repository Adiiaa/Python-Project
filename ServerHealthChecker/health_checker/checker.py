import requests
import time


def check_server(url):

    start = time.perf_counter()

    try:
        response = requests.get(url, timeout=5)

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

    except requests.RequestException:

        return {
            "url": url,
            "status_code": None,
            "response_time": None,
            "healthy": False,
            "json_ok": False,
            "slow": False
        }


def check_all_servers(servers):
    return [check_server(server) for server in servers]