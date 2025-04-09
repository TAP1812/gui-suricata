from flask import Flask, render_template
from core.suricata_reader import get_alerts
from core.traffic_analyzer import get_traffic_data
from core.rules_manager import get_rules
from config.setttings import SURICATA_LOG_PATH, SURICATA_RULES_PATH, FLASK_PORT
app = Flask(__name__)

@app.route('/')
def dashboard():
    alerts = get_alerts()
    traffic_data = get_traffic_data()
    return render_template('dashboard.html', alerts=alerts, traffic_data=traffic_data)

if __name__ == '__main__':
    app.run(host='localhost', port=FLASK_PORT)