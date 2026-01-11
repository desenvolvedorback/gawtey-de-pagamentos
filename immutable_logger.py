import os
from datetime import datetime

LOGFILE = os.getenv("IMMUTABLE_LOG", "/var/log/gateway_immutable.log")

def append_log(event_type: str, payload: dict):
    entry = {
        "ts": datetime.utcnow().isoformat(),
        "type": event_type,
        "payload": payload
    }
    os.makedirs(os.path.dirname(LOGFILE), exist_ok=True)
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(str(entry) + "\n")
