import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Ransomware Attack Chain Simulator",
    page_icon="🛡️",
    layout="wide"
)

STAGES = {
    "1. Initial Entry": {
        "vector": "Phishing email",
        "story": "A hospital employee receives a suspicious email.",
        "prevention": [
            "Verify the sender before opening attachments.",
            "Never enter passwords through unknown links.",
            "Report suspicious emails to IT Security."
        ]
    },
    "2. Execution": {
        "vector": "Suspicious file execution",
        "story": "A simulated suspicious file triggers a security alert.",
        "prevention": [
            "Block suspicious executable attachments.",
            "Use updated endpoint protection.",
            "Avoid running unknown programs."
        ]
    },
    "3. Discovery": {
        "vector": "Simulated system discovery",
        "story": "The monitoring team reviews unusual activity.",
        "prevention": [
            "Monitor unusual account and system activity.",
            "Apply least-privilege access.",
            "Review security logs regularly."
        ]
    },
    "4. Impact": {
        "vector": "Simulated file-locking threat",
        "story": "A warning indicates a possible ransomware incident. "
                 "No files are encrypted or modified by this demo.",
        "prevention": [
            "Maintain offline backups.",
            "Use network segmentation.",
            "Keep endpoint detection and response enabled."
        ]
    },
    "5. Detection & Response": {
        "vector": "Security alert and incident response",
        "story": "The security team investigates the alert and follows "
                 "the incident response procedure.",
        "prevention": [
            "Follow the organization's incident response plan.",
            "Isolate affected devices when authorized.",
            "Preserve logs and notify the security team."
        ]
    }
}

st.title("🛡️ Ransomware Attack Chain Simulator")
st.caption(
    "Healthcare cybersecurity awareness • Educational simulation only"
)

st.warning(
    "SAFE DEMO: This application does not encrypt, delete, "
    "or modify files and does not perform real attacks."
)

with st.sidebar:
    st.header("Navigation")
    page = st.radio(
        "Choose a section",
        [
            "Overview",
            "Attack Stages",
            "Knowledge Quiz",
            "Incident Report"
        ]
    )
    st.divider()
    st.caption("Project: Cybersecurity Awareness")

if page == "Overview":
    st.subheader("Project Overview")
    st.write(
        "Learn how ransomware incidents may develop in a healthcare "
        "environment and how security teams can prevent and respond "
        "to them."
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Learning Stages", len(STAGES))
    col2.metric("Environment", "Healthcare")
    col3.metric("Real File Changes", "None")

    st.subheader("Learning Objectives")
    st.markdown(
        """
        - Understand common ransomware warning signs.
        - Learn practical prevention methods.
        - Understand detection and incident response.
        - Practice cybersecurity awareness using a safe simulation.
        """
    )

elif page == "Attack Stages":
    st.subheader("Attack Chain Learning Module")
    selected = st.selectbox("Select a stage", list(STAGES.keys()))
    details = STAGES[selected]

    st.markdown(f"### {selected}")
    st.info(f"**Threat vector:** {details['vector']}")
    st.write(details["story"])

    st.markdown("#### Prevention and Protection")
    for tip in details["prevention"]:
        st.markdown(f"- {tip}")

elif page == "Knowledge Quiz":
    st.subheader("Cybersecurity Knowledge Quiz")

    questions = [
        {
            "question": "What should you do with a suspicious email?",
            "options": [
                "Open every attachment",
                "Verify the sender and report it",
                "Forward it to everyone"
            ],
            "answer": "Verify the sender and report it"
        },
        {
            "question": "Which backup approach improves ransomware resilience?",
            "options": [
                "Keep only one backup on the same computer",
                "Avoid backups",
                "Maintain tested offline backups"
            ],
            "answer": "Maintain tested offline backups"
        },
        {
            "question": "What should you do after a suspected incident?",
            "options": [
                "Ignore the alert",
                "Follow the incident response plan",
                "Delete all security logs"
            ],
            "answer": "Follow the incident response plan"
        }
    ]

    with st.form("knowledge_quiz"):
        answers = []
        for i, item in enumerate(questions):
            st.markdown(f"**{i + 1}. {item['question']}**")
            answers.append(
                st.radio(
                    "Choose your answer",
                    item["options"],
                    key=f"question_{i}",
                    index=None
                )
            )

        submitted = st.form_submit_button("Submit Answers")

    if submitted:
        if any(answer is None for answer in answers):
            st.warning("Please answer all questions first.")
        else:
            score = sum(
                answer == item["answer"]
                for answer, item in zip(answers, questions)
            )
            st.success(f"Your score: {score}/{len(questions)}")
            if score == len(questions):
                st.balloons()
                st.write("Excellent! You understand the key safety steps.")
            else:
                st.info("Review the prevention tips and try again.")

elif page == "Incident Report":
    st.subheader("Generate Educational Incident Report")

    department = st.selectbox(
        "Department",
        ["Radiology", "Emergency", "Laboratory", "Administration"]
    )

    if st.button("Generate Report"):
        report = [
            "RANSOMWARE AWARENESS SIMULATION REPORT",
            "=" * 42,
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "Environment: Healthcare (educational scenario)",
            f"Department: {department}",
            "Status: Simulated scenario only",
            "",
            "STAGES REVIEWED"
        ]

        for name, details in STAGES.items():
            report.append(f"\n{name}")
            report.append(f"Threat vector: {details['vector']}")
            report.append(f"Scenario: {details['story']}")
            report.append("Prevention:")
            for tip in details["prevention"]:
                report.append(f"- {tip}")

        report.extend([
            "",
            "SAFETY STATEMENT",
            "No real files were encrypted, deleted, or damaged.",
            "This report is for cybersecurity awareness and education."
        ])

        report_text = "\n".join(report)
        st.text_area("Report Preview", report_text, height=350)

        st.download_button(
            "Download Report",
            data=report_text,
            file_name="ransomware_awareness_report.txt",
            mime="text/plain"
        )

st.divider()
st.caption("Educational project • Safe simulation • No real attack actions")