from health_checker.config import load_servers
from health_checker.checker import check_server
from health_checker.formatter import format_result


def main():

    servers = load_servers()

    failed_services = []

    for server in servers:

        result = check_server(server)

        print(format_result(result))

        if not result["healthy"]:
            failed_services.append(server)

    print()

    if failed_services:
        print("Failed services:")

        for service in failed_services:
            print(service)
    else:
        print("No failed services.")


if __name__ == "__main__":
    main()