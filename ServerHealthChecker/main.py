from health_checker.config import load_servers
from health_checker.checker import check_all_servers
from health_checker.formatter import format_result
from health_checker.alerts import send_alert


def main():

    servers = load_servers()

    results = check_all_servers(servers)

    failed_services = []

    for result in results:

        print(format_result(result))

        if not result["healthy"]:
            failed_services.append(result["url"])

    print()

    if failed_services:
        print("Failed services:")
        for f in failed_services:
            print(f)
    else:
        print("No failed services.")

    return failed_services


if __name__ == "__main__":

    failed_services = main()

    send_alert(failed_services)