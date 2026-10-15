from pathlib import Path
from datetime import datetime


def generate_report():
    log_file = Path("logs/events.log")
    report_file = Path("reports/attack_report.txt")

    if not log_file.exists():
        print("[ERROR] events.log not found.")
        return

    events = log_file.read_text(encoding="utf-8").splitlines()

    report = []
    report.append("=" * 60)
    report.append("        RANSOMWARE ATTACK SIMULATION REPORT")
    report.append("=" * 60)
    report.append("")
    report.append(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("Scenario: Healthcare Environment")
    report.append("Mode: Safe Simulation")
    report.append("")
    report.append("DETECTED EVENTS")
    report.append("-" * 60)

    for event in events:
        report.append(event)

    report.append("")
    report.append("-" * 60)
    report.append(f"Total Events Detected: {len(events)}")
    report.append("")
    report.append("No real files were encrypted, deleted, or damaged.")
    report.append("=" * 60)

    report_file.write_text("\n".join(report), encoding="utf-8")

    print("[+] Report generated successfully.")
    print(f"[+] Report saved to: {report_file}")


if __name__ == "__main__":
    generate_report()