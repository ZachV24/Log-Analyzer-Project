# Log-Analyzer-Project

This project is a Python-based log analyzer designed to detect basic security threats by parsing and analyzing system or application log files. The tool reads log data line by line, identifies patterns associated with suspicious activity, and generates alerts based on predefined rules.

At its core, the analyzer uses regular expressions to extract relevant information such as IP addresses from log entries. It specifically detects repeated failed login attempts, which may indicate a brute force attack. The system tracks the number of failed attempts per IP address and triggers an alert when a configurable threshold is exceeded. In addition, it flags any activity involving known suspicious IP addresses defined in a configuration file.

The project is modular, with separate components for log parsing, analysis, and report generation. Results are displayed in the terminal and saved to a report file, making it easy to review findings. Configuration settings such as detection thresholds and flagged IPs are stored in a JSON file, allowing users to adjust behavior without modifying the code.

This project demonstrates key cybersecurity concepts including log analysis, pattern matching, and basic intrusion detection. It also reflects real-world practices used in Security Operations Centers (SOCs), where automated tools monitor logs for indicators of compromise.

Overall, the log analyzer serves as a foundational example of how security monitoring systems work and provides a platform for further expansion into more advanced detection and alerting capabilities.
