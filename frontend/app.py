import streamlit as st
import requests

st.set_page_config(page_title="Biometric Face Attendance", layout="wide")

st.title("👤 Biometric Face Attendance System")
st.markdown("High-speed facial embedding extraction, cosine similarity matching, and attendance persistence.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Simulate Facial Probe Ingest")
    user_choice = st.selectbox("Select Known Subject or Anomaly", ["Sarah Connor (USR-101)", "John Doe (USR-102)", "Unknown Intruder"])
    threshold = st.slider("Cosine Match Threshold", 0.50, 0.95, 0.75)

    if st.button("Submit Biometric Verification Frame", type="primary"):
        probe = [0.35, 0.62, -0.41, 0.55] if "Sarah" in user_choice else ([-0.12, 0.81, 0.45, -0.32] if "John" in user_choice else [0.89, -0.71, 0.22, 0.11])
        try:
            res = requests.post("http://localhost:8000/api/v1/attendance/verify", json={"probe_embedding": probe, "confidence_threshold": threshold}, timeout=5)
            if res.status_code == 200:
                st.session_state["p18a_res"] = res.json()
                st.success("Verification Completed!")
            else:
                st.error(res.text)
        except Exception:
            st.warning("Backend offline. Executing client-side fallback.")
            st.session_state["p18a_res"] = {
                "record_id": "REC-SIM001",
                "user_id": "USR-101" if "Sarah" in user_choice else "UNKNOWN",
                "full_name": "Sarah Connor" if "Sarah" in user_choice else "Unidentified Individual",
                "status": "VERIFIED_PRESENT" if "Sarah" in user_choice else "ACCESS_DENIED",
                "confidence": 0.99 if "Sarah" in user_choice else 0.23,
                "timestamp": "2026-08-28T09:00:00Z"
            }

with col2:
    if "p18a_res" in st.session_state:
        r = st.session_state["p18a_res"]
        st.subheader("Attendance Verification Outcome")
        if r["status"] == "VERIFIED_PRESENT":
            st.success(f"Verified: **{r['full_name']}** (`{r['user_id']}`)")
        else:
            st.error(f"Denied: **{r['full_name']}**")
        st.metric("Match Confidence", f"{r['confidence'] * 100:.2f}%")
        st.write(f"Logged Transaction ID: `{r['record_id']}`")
