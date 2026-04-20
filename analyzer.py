import re
from collections import defaultdict

FAILED_LOGIN_PATTERN = re.compile(r"Failed login from (\d+\.\d+\.\d+\.\d+)")

def analyze_logs(log_lines, config):
    failed_attempts = defaultdict(int)
    alerts = []

    for line in log_lines:
        match = FAILED_LOGIN_PATTERN.search(line)
        if match:
            ip = match.group(1)
            failed_attempts[ip] += 1

            # Threshold detection
            if failed_attempts[ip] == config["failed_login_threshold"]:
                alerts.append(f"🚨 Possible brute force attack from {ip}")

        # Suspicious IP detection
        for ip in config["suspicious_ips"]:
            if ip in line:
                alerts.append(f"⚠️ Suspicious IP detected: {ip}")

    return alerts