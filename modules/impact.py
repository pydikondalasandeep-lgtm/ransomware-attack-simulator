from pathlib import Path


def simulate_impact():
    print("\n===== IMPACT SIMULATION =====")

    test_folder = Path("test_data")

    if not test_folder.exists():
        print("[ERROR] Test data folder not found.")
        return

    files = list(test_folder.glob("*"))

    print(f"[+] Test files found: {len(files)}")

    for file in files:
        if file.is_file():
            print(f"[SIMULATED IMPACT] {file.name}")

    print("\n[+] Simulated ransomware impact detected")
    print("[+] No files were encrypted or deleted")
    print("[ALERT] Impact stage simulated successfully.")


if __name__ == "__main__":
    simulate_impact()