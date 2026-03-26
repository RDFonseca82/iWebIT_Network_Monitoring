
import psutil
def interface_stats():
    interfaces = []
    stats = psutil.net_io_counters(pernic=True)
    for iface in stats:
        interfaces.append({
            "Name": iface,
            "RX_MB": stats[iface].bytes_recv / 1024 / 1024,
            "TX_MB": stats[iface].bytes_sent / 1024 / 1024,
            "Errors": stats[iface].errin + stats[iface].errout,
            "Dropped": stats[iface].dropin + stats[iface].dropout
        })
    return interfaces
