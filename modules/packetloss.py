
import os
from core.system import get_gateway

def packetloss_test(config):
    gw = get_gateway()
    result = os.popen(f"ping -c 10 {gw} | grep loss").read()
    try:
        loss = result.split(',')[2].strip()
        return loss
    except:
        return "0%"
