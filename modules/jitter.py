import subprocess

def jitter_test(config):
    try:
        gw = subprocess.check_output(
            "ip route | grep default | awk '{print $3}'",
            shell=True
        ).decode().strip()

        result = subprocess.check_output(
            ["ping", "-c", "10", gw],
            stderr=subprocess.DEVNULL
        ).decode()

        line = [l for l in result.split("\n") if "min/avg" in l]
        if line:
            values = line[0].split("=")[1].split("/")
            return float(values[3])
    except:
        pass

    return 0
