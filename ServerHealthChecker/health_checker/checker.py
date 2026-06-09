import requests
import time


def check_server(url):
    start = time.perf_counter()

    try:
        response = requests.get(url, timeout=5)

        elapsed = (
            time.perf_counter() - start
        ) * 1000

        healthy = (
            200 <= response.status_code < 300
        )

        return {
            "url": url,
            "status_code": response.status_code,
            "response_time": round(elapsed, 2),
            "healthy": healthy
        }

    except requests.RequestException:

        return {
            "url": url,
            "status_code": None,
            "response_time": None,
            "healthy": False
        }