import time
import socket
from datetime import datetime

from core.config import load_config
from core.logger import log
from core.api import send_to_api
from core.system import get_local_ip, get_mac, get_gateway

from modules.latency import latency_test
from modules.packetloss import packetloss_test
from modules.jitter import jitter_test
from modules.dns import dns_test
from modules.http import http_test
from modules.bandwidth import bandwidth_test
from modules.interfaces import interface_stats
from modules.connections import connection_count
from modules.health import network_health


config = load_config()


def build_data():
    data = {}

    data["UniqueID"] = config["UniqueID"]
    data["IDSync"] = config["IDSync"]
    data["Hostname"] = socket.gethostname()
    data["LocalIP"] = get_local_ip()
    data["MAC"] = get_mac()
    data["GatewayIP"] = get_gateway()
    data["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    latency = latency_test(config)
    packetloss = packetloss_test(config)
    jitter = jitter_test(config)
    dns = dns_test(config)
    http = http_test(config)
    bandwidth = bandwidth_test()
    interfaces = interface_stats()
    connections = connection_count()

    health = network_health(latency, interfaces, packetloss)

    data["Latency"] = latency
    data["PacketLoss"] = packetloss
    data["Jitter"] = jitter
    data["DNS"] = dns
    data["HTTP"] = http
    data["Bandwidth"] = bandwidth
    data["Interfaces"] = interfaces
    data["Connections"] = connections
    data["NetworkHealth"] = health

    return data


def main():
    log("iWebIT Network Monitoring Agent Started")

    while True:
        try:
            data = build_data()
            send_to_api(config["API"], data)
            log("Data sent to API")
        except Exception as e:
            log("Error: " + str(e))

        time.sleep(config["Intervals"]["Minimal"])


if __name__ == "__main__":
    main()
