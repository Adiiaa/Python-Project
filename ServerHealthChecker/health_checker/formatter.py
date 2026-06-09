def format_result(result):

    if result["status_code"] is None:
        return f'{result["url"]} — TIMEOUT'

    status = "OK" if result["healthy"] else "DOWN"

    output = (
        f'{result["url"]} — '
        f'{status} ({result["status_code"]}) — '
        f'{result["response_time"]}ms'
    )

    if result["slow"]:
        output += " [slow]"

    return output