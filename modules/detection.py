from datetime import datetime
from pathlib import Path


def log_event(message):
    log_file = Path("logs/events.log")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")


def detect_threats():
    print("\n===== THREAT DETECTION =====")

    threats = [
        "Phishing attempt detected",
        "Initial access detected",
        "Suspicious execution detected",
        "Persistence attempt detected",
        "System discovery detected",
        "Ransomware impact detected"
    ]

    for threat in threats:
        print("[ALERT]", threat)
        log_event(threat)

    print("\n[+] Threat detection completed")
    print("[+] Events saved to logs/events.log")


if __name__ == "__main__":
    detect_threats()