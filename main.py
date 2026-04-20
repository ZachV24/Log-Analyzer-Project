import json
from analyzer import analyze_logs
from logger import read_log_file, write_report

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def main():
    config = load_config()
    log_lines = read_log_file("logs/sample.log")

    alerts = analyze_logs(log_lines, config)

    write_report(alerts)

    print("\n=== Alerts ===")
    for alert in alerts:
        print(alert)

if __name__ == "__main__":
    main()