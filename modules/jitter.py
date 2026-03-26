
import os
from core.system import get_gateway

def jitter_test(config):
    gw = get_gateway()
    result = os.popen(f"ping -c 10 {gw} | tail -1| awk '{{print $4}}'").read()
    try:
        values = result.split('/')[3]
        return float(values)
    except:
        return 0
