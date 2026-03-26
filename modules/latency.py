import subprocess

def get_latency(host):
    try:
        result = subprocess.check_output(
            ["ping", "-c", "4", host],
            stderr=subprocess.DEVNULL
        ).decode()

        line = [l for l in result.split("\n") if "min/avg" in l]
        if line:
            values = line[0].split("=")[1].split("/")
            return float(values[1])
    except:
        pass

    return 0


def latency_test(config):
    data = {}

    try:
        import subprocess
        gw = subprocess.check_output(
            "ip route | grep default | awk '{print $3}'",
            shell=True
        ).decode().strip()

        data["Gateway"] = get_latency(gw)
    except:
        data["Gateway"] = 0

    internet = []
    for host in config["PingHosts"]:
        internet.append(get_latency(host))

    if internet:
        data["Internet"] = sum(internet) / len(internet)
    else:
        data["Internet"] = 0

    return data
