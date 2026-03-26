
import os
from core.system import get_gateway

def get_latency(host):
    result = os.popen(f"ping -c 4 {host} | tail -1| awk '{{print $4}}'").read()
    if result:
        return float(result.split('/')[1])
    return 0

def latency_test(config):
    data = {}
    gw = get_gateway()
    data["Gateway"] = get_latency(gw)

    internet = []
    for host in config["PingHosts"]:
        internet.append(get_latency(host))

    data["Internet"] = sum(internet) / len(internet)
    return data
