import streamlit as st

st.set_page_config(
page_title="Healthcare Ransomware Simulator",
page_icon="🛡️",
layout="wide"
)

st.title("🛡️ Healthcare Ransomware Attack Simulator")
st.subheader("Cybersecurity Awareness and Education")

st.warning(
"Educational simulation only. No real files are encrypted or damaged."
)

department = st.sidebar.selectbox(
"Select Department",
["Radiology", "Emergency", "Cardiology", "IT Security"]
)

st.sidebar.success(f"Selected: {department}")

st.markdown("## Attack Chain Simulation")

stages = {
"Stage 1: Phishing Email": {
"story": f"A suspicious email reaches the {department} department.",
"prevention": [
"Verify the sender's email address.",
"Do not open unexpected attachments.",
"Report suspicious emails to IT Security."
]
},
"Stage 2: Initial Access": {
"story": "A simulated user interacts with a suspicious attachment.",
"prevention": [
"Use multi-factor authentication.",
"Keep software updated.",
"Use endpoint protection."
]
},
"Stage 3: Ransomware Impact": {
"story": "A simulated alert indicates a possible ransomware incident.",
"prevention": [
"Maintain offline backups.",
"Separate critical healthcare systems.",
"Follow the incident response plan."
]
},
"Stage 4: Detection and Response": {
"story": "The security team investigates the simulated alert.",
"prevention": [
"Isolate affected systems when authorized.",
"Notify the incident response team.",
"Restore data from verified backups."
]
}
}

selected_stage = st.selectbox(
"Choose an attack stage",
list(stages.keys())
)

stage = stages[selected_stage]

st.info(stage["story"])

st.markdown("### 🛡️ Prevention Tips")

for tip in stage["prevention"]:
st.write(f"✅ {tip}")

if st.button("Generate Awareness Report"):
st.success("Awareness report generated successfully.")

st.text_area(
    "Simulation Report",
    f"""Healthcare Ransomware Awareness Report

Department: {department}
Stage: {selected_stage}

Scenario:
{stage['story']}

Prevention Measures:

- """ + "\n- ".join(stage["prevention"]),
  height=250
  )

st.divider()
st.caption("Cybersecurity Awareness Project | Safe Educational Simulation")