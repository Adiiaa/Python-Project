import json


def load_servers():
    with open("config.json", "r") as file:
        config = json.load(file)

    servers = config["servers"]

    print(f"Loaded {len(servers)} servers")

    return servers