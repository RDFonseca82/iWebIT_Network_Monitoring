
import psutil, time
def bandwidth_test():
    net1 = psutil.net_io_counters()
    time.sleep(1)
    net2 = psutil.net_io_counters()
    download = (net2.bytes_recv - net1.bytes_recv) * 8 / 1024 / 1024
    upload = (net2.bytes_sent - net1.bytes_sent) * 8 / 1024 / 1024
    return {"DownloadMbps": download, "UploadMbps": upload}
