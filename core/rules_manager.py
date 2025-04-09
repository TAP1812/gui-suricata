from config.setttings import SURICATA_RULES_PATH

def get_rules():
    rules = []
    with open(f"{SURICATA_RULES_PATH}/local.rules", 'r') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                rules.append(line.strip())
    return rules