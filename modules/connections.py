import psutil
def connection_count():
    return len(psutil.net_connections())
