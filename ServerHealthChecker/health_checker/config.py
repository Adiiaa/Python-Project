import json
import os


def load_servers():

    env_servers = os.getenv("SERVERS")

    if env_servers:
        servers = env_servers.split(",")
        print(f"Loaded {len(servers)} servers from ENV")
        return servers

    try:
        with open("config.json", "r") as file:
            config = json.load(file)

        servers = config["servers"]
        print(f"Loaded {len(servers)} servers from file")
        return servers

    except FileNotFoundError:
        raise Exception("No SERVERS env var or config.json found")