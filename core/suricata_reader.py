import json
from config.setttings import SURICATA_LOG_PATH

def get_alerts(limit=10):
    alerts = []
    try:
        with open(SURICATA_LOG_PATH, 'r') as f:
            for line in f:
                try:
                    event = json.loads(line)
                    if event.get('event_type') == 'alert':
                        alerts.append({
                            'time': event['timestamp'],
                            'src_ip': event['src_ip'],
                            'dest_ip': event['dest_ip'],
                            'type': event['alert']['signature']
                        })
                except:
                    continue
    except FileNotFoundError:
        print("Log file not found!")
    return alerts[-limit:]