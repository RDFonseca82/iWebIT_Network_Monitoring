import subprocess

def packetloss_test(config):
    try:
        gw = subprocess.check_output(
            "ip route | grep default | awk '{print $3}'",
            shell=True
        ).decode().strip()

        result = subprocess.check_output(
            ["ping", "-c", "10", gw],
            stderr=subprocess.DEVNULL
        ).decode()

        for line in result.split("\n"):
            if "packet loss" in line:
                return line.split(",")[2].strip()
    except:
        pass

    return "0%"
