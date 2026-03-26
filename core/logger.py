
from datetime import datetime
import json

def log(message):
    try:
        with open("config.json") as f:
            config = json.load(f)
        if config["Log"] == 1:
            with open("logs/agent.log", "a") as log_file:
                log_file.write(f"{datetime.now()} - {message}\n")
    except:
        pass
