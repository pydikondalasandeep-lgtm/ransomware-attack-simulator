from simulation.simulator import run_simulation


def show_banner():
    print("\n" + "=" * 60)
    print("        RANSOMWARE ATTACK CHAIN SIMULATOR")
    print("=" * 60)
    print("        Healthcare Environment")
    print("        Safe Cybersecurity Simulation")
    print("=" * 60)


def show_stages():
    print("\n========== ATTACK CHAIN STAGES ==========")

    stages = [
        "1. Reconnaissance",
        "2. Phishing",
        "3. Initial Access",
        "4. Execution",
        "5. Persistence",
        "6. Discovery",
        "7. Impact",
        "8. Detection"
    ]

    for stage in stages:
        print(stage)

    print("==========================================")


def main():

    while True:

        show_banner()

        print("\n1. Run Full Simulation")
        print("2. View Attack Stages")
        print("3. Generate Report")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            print("\n[+] Starting full simulation...\n")

            run_simulation()

            print("\n[+] Full simulation completed.")
            input("\nPress Enter to return to the main menu...")

        elif choice == "2":

            show_stages()

            input("\nPress Enter to return to the main menu...")

        elif choice == "3":

            from reports.report_generator import generate_report

            print("\n[+] Generating report...\n")

            generate_report()

            input("\nPress Enter to return to the main menu...")

        elif choice == "4":

            print("\n" + "=" * 60)
            print("Exiting Ransomware Attack Chain Simulator...")
            print("=" * 60)

            break

        else:

            print("\n[ERROR] Invalid choice.")
            print("[INFO] Please enter a number from 1 to 4.")

            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()