import requests


def check_server(url):
    response = requests.get(url)

    return {
        "url": url,
        "status_code": response.status_code
    }