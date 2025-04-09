from config.setttings import SURICATA_LOG_PATH, SURICATA_RULES_PATH
from core.suricata_reader import get_alerts
from core.rules_manager import get_rules
from core.traffic_analyzer import get_traffic_data

def test_suricata_reader():
    # Test xem có thể đọc được file log không
    alerts = get_alerts()
    assert isinstance(alerts, list), "get_alerts should return a list"
    assert len(alerts) <= 10, "get_alerts should return at most 10 alerts"
    
    print(len(alerts), "alerts")
    print(alerts)
    
def test_rules_manager():
    # Test xem có thể đọc được file rules không
    rules = get_rules()
    assert isinstance(rules, list), "get_rules should return a list"
    assert len(rules) > 0, "get_rules should return at least one rule"
    
    print(len(rules), "rules")
    print(rules)
    
test_rules_manager()