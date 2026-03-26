import socket
import uuid
import subprocess

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def get_mac():
    mac = uuid.getnode()
    mac = ':'.join(('%012X' % mac)[i:i+2] for i in range(0, 12, 2))
    return mac

def get_gateway():
    route = subprocess.check_output("ip route | grep default", shell=True).decode()
    return route.split()[2]
