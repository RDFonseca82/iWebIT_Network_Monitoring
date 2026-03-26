
import socket, time
def dns_lookup(domain):
    start = time.time()
    socket.gethostbyname(domain)
    end = time.time()
    return (end - start) * 1000

def dns_test(config):
    results = {}
    for domain in config["DNSDomains"]:
        results[domain] = dns_lookup(domain)
    return results
