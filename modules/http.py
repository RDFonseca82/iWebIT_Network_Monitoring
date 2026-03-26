
import requests, time
def http_time(url):
    start = time.time()
    requests.get(url, timeout=5)
    end = time.time()
    return (end - start) * 1000

def http_test(config):
    results = {}
    for url in config["HTTPTest"]:
        results[url] = http_time(url)
    return results
