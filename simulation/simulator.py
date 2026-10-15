from pathlib import Path
from datetime import datetime
import time


LOG_FILE = Path("logs/events.log")


def log_event(message):
    LOG_FILE.parent.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")


def pause():
    time.sleep(1)


def run_simulation():

    print("\n" + "=" * 65)
    print("          RANSOMWARE ATTACK CHAIN SIMULATION")
    print("=" * 65)
    print("Scenario : Hospital / Healthcare Environment")
    print("Mode     : SAFE SIMULATION")
    print("=" * 65)

    input("\nPress ENTER to start the simulation...")

    # --------------------------------------------------
    # STAGE 1
    # --------------------------------------------------

    print("\n[STAGE 1] RECONNAISSANCE")
    print("-" * 65)

    print("[SIMULATION] Attacker gathers information about the hospital.")
    print("[SIMULATION] Target environment: Hospital network")
    print("[SIMULATION] Possible target: Employee workstation")

    log_event("Reconnaissance activity simulated against healthcare environment.")
    pause()

    # --------------------------------------------------
    # STAGE 2
    # --------------------------------------------------

    print("\n[STAGE 2] PHISHING")
    print("-" * 65)

    print("[SIMULATION] Fake urgent email prepared.")
    print("[SIMULATION] Example:")
    print("           Subject: URGENT - Hospital Account Verification")
    print("           Sender : simulated-attacker@example.test")
    print()
    print("[SIMULATION] No real email was sent.")
    print("[SIMULATION] User interaction is simulated only.")

    log_event("Controlled phishing attempt simulated. No real email sent.")
    pause()

    # --------------------------------------------------
    # STAGE 3
    # --------------------------------------------------

    print("\n[STAGE 3] INITIAL ACCESS")
    print("-" * 65)

    print("[SIMULATION] Employee interaction with the fake message detected.")
    print("[SIMULATION] Attacker access is now simulated.")
    print("[SIMULATION] No real system access occurred.")

    log_event("Initial access simulated through phishing scenario.")
    pause()

    # --------------------------------------------------
    # STAGE 4
    # --------------------------------------------------

    print("\n[STAGE 4] EXECUTION")
    print("-" * 65)

    print("[SIMULATION] Suspicious ransomware process starts.")
    print("[SIMULATION] Process name: simulated_ransomware.exe")
    print("[SIMULATION] No real executable was created or executed.")

    log_event("Ransomware execution behavior simulated.")
    pause()

    # --------------------------------------------------
    # STAGE 5
    # --------------------------------------------------

    print("\n[STAGE 5] PERSISTENCE")
    print("-" * 65)

    print("[SIMULATION] Attacker attempts to maintain access.")
    print("[SIMULATION] Persistence technique is represented conceptually.")
    print("[SIMULATION] No real startup settings were modified.")

    log_event("Persistence behavior simulated safely.")
    pause()

    # --------------------------------------------------
    # STAGE 6
    # --------------------------------------------------

    print("\n[STAGE 6] DISCOVERY")
    print("-" * 65)

    print("[SIMULATION] Attacker searches for valuable healthcare data.")
    print()
    print("        Target data:")
    print("        - Patient records")
    print("        - Medical reports")
    print("        - Hospital documents")
    print("        - Backup information")

    print()
    print("[SIMULATION] These are dummy targets only.")
    print("[SIMULATION] No real files were accessed.")

    log_event("Discovery of simulated healthcare data completed.")
    pause()

    # --------------------------------------------------
    # STAGE 7
    # --------------------------------------------------

    print("\n[STAGE 7] RANSOMWARE IMPACT")
    print("-" * 65)

    print("[SIMULATION] Ransomware impact phase started.")
    print()
    print("[SIMULATION] Files that WOULD be affected:")
    print("        patient_records.txt")
    print("        medical_reports.txt")
    print("        hospital_documents.txt")

    print()
    print("[SAFE MODE] These files are NOT actually encrypted.")
    print("[SAFE MODE] No real data has been modified.")

    log_event("Ransomware impact simulated. No real files encrypted.")
    pause()

    # --------------------------------------------------
    # RANSOM DEMAND
    # --------------------------------------------------

    print("\n" + "=" * 65)
    print("                    RANSOM DEMAND")
    print("=" * 65)

    print()
    print("        YOUR FILES HAVE BEEN SIMULATED")
    print("        AS ENCRYPTED!")
    print()
    print("        Simulated ransom demand : 0.05 BTC")
    print("        Payment status          : NOT PAID")
    print("        Payment address         : SIMULATED-ADDRESS")
    print("        Deadline                : 48 HOURS")
    print()
    print("        ⚠ THIS IS NOT A REAL PAYMENT REQUEST.")
    print("        ⚠ NO CRYPTOCURRENCY IS SENT.")
    print("        ⚠ NO REAL FILES ARE ENCRYPTED.")
    print("=" * 65)

    log_event("Simulated ransom demand generated: 0.05 BTC. No payment made.")
    pause()

    # --------------------------------------------------
    # STAGE 8
    # --------------------------------------------------

    print("\n[STAGE 8] DETECTION")
    print("-" * 65)

    print("[DETECTION] Suspicious ransomware behavior detected.")
    print("[DETECTION] Multiple ransomware indicators identified.")
    print("[DETECTION] Security alert generated.")

    log_event("Ransomware behavior detected by simulated security monitoring.")
    pause()

    # --------------------------------------------------
    # INCIDENT RESPONSE
    # --------------------------------------------------

    print("\n[INCIDENT RESPONSE]")
    print("-" * 65)

    print("[RESPONSE] Suspicious activity identified.")
    print("[RESPONSE] Simulated infected workstation isolated.")
    print("[RESPONSE] Attacker's simulated access terminated.")
    print("[RESPONSE] Security incident recorded.")
    print("[RESPONSE] Recovery process can now begin.")

    log_event("Incident response simulated. Host isolated and access terminated.")
    pause()

    # --------------------------------------------------
    # FINAL RESULT
    # --------------------------------------------------

    print("\n" + "=" * 65)
    print("                 SIMULATION COMPLETE")
    print("=" * 65)

    print()
    print("Attack Path:")
    print("Reconnaissance")
    print("      ↓")
    print("Phishing")
    print("      ↓")
    print("Initial Access")
    print("      ↓")
    print("Execution")
    print("      ↓")
    print("Persistence")
    print("      ↓")
    print("Discovery")
    print("      ↓")
    print("Ransomware Impact")
    print("      ↓")
    print("Ransom Demand")
    print("      ↓")
    print("Detection")
    print("      ↓")
    print("Incident Response")

    print()
    print("RESULT:")
    print("✔ Attack chain demonstrated")
    print("✔ Ransom demand simulated")
    print("✔ Detection successful")
    print("✔ Incident response simulated")
    print("✔ No real files encrypted")
    print("✔ No real payment made")
    print("✔ No real email sent")

    print("=" * 65)

    log_event("Full ransomware attack-chain simulation completed successfully.")