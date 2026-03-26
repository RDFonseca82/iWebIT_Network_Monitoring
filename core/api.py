
import requests
import json
def send_to_api(url, data):
    headers = {'Content-Type': 'application/json'}
    requests.post(url, data=json.dumps(data), headers=headers, timeout=10)
