import requests
import time


def check_server(url):
    start = time.perf_counter()

    response = requests.get(url)

    end = time.perf_counter()

    response_time = (end - start) * 1000

    return {
        "url": url,
        "status_code": response.status_code,
        "response_time": round(response_time, 2)
    }