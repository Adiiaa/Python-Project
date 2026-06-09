from health_checker.checker import check_server

result = check_server(
    "https://httpbin.org/status/200"
)

print(result)