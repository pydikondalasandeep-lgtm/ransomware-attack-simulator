Ransomware Attack Chain Simulator

Overview

The Ransomware Attack Chain Simulator is a safe cybersecurity education project that demonstrates the major stages of a ransomware attack in a controlled environment.

The project does not send real phishing emails, encrypt real files, delete data, or perform attacks against real systems.

Project Objective

The main objective is to help students understand how a ransomware attack can progress through multiple stages and how security monitoring and detection can identify suspicious activity.

Attack Chain

1. Reconnaissance
2. Phishing
3. Initial Access
4. Execution
5. Persistence
6. Discovery
7. Impact
8. Detection

Healthcare Scenario

The simulator uses a fictional healthcare environment for demonstration.

A dummy file such as "patient_records.txt" represents sensitive hospital data. The file is used only for simulation and is not encrypted or deleted.

Main Features

- Menu-driven simulator
- Ransomware attack-chain demonstration
- Controlled phishing simulation
- Dummy healthcare test data
- Impact simulation
- Threat detection
- Security event logging
- Automated attack report generation
- Safe execution without damaging real files

Project Structure

ransomware attack simulator/
│
├── app.py
│
├── modules/
│   ├── reconnaissance.py
│   ├── phishing.py
│   ├── initial_access.py
│   ├── execution.py
│   ├── persistence.py
│   ├── discovery.py
│   ├── impact.py
│   └── detection.py
│
├── simulation/
│   ├── __init__.py
│   └── simulator.py
│
├── test_data/
│   └── patient_records.txt
│
├── logs/
│   └── events.log
│
└── reports/
    ├── report_generator.py
    └── attack_report.txt

How to Run

Open the terminal in the project folder and run:

python app.py

The application provides a menu:

1. Run Full Simulation
2. View Attack Stages
3. Generate Report
4. Exit

Safety

This project is designed strictly for cybersecurity education and controlled demonstration.

No real ransomware is deployed and no real user data is targeted.

Technologies Used

- Python
- Python Modules
- File Handling
- Logging
- Pathlib
- Datetime
- Terminal-based User Interface

Expected Outcome

The project demonstrates the ransomware attack lifecycle and shows how suspicious activity can be detected, logged, and converted into a security report.

Author

Cybersecurity Student Project