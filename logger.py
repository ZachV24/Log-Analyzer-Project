import os

def read_log_file(path):
    if not os.path.exists(path):
        print(f"Log file not found: {path}")
        return []
    
    with open(path, "r") as f:
        return f.readlines()

def write_report(alerts):
    if not os.path.exists("reports"):
        os.makedirs("reports")

    with open("reports/report.txt", "w") as f:
        if alerts:
            for alert in alerts:
                f.write(alert + "\n")
        else:
            f.write("No suspicious activity detected.\n")

    print("Report generated: reports/report.txt")