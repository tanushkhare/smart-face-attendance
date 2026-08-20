import streamlit as st
import requests

st.title("☸️ Project 18: Multi-Service Orchestration Hub")
if st.button("Inspect Stack Services"):
    res = requests.get("http://127.0.0.1:8000/api/compose-status")
    if res.status_code == 200:
        data = res.json()
        st.metric("Active Services Count", data["services_active"])
        st.info(f"Orchestrator Engine: {data['orchestrator']}")
        st.write("**Running Containers:**", data["active_services"])