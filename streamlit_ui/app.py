import streamlit as st
import requests
import os 

st.title("🩺 AI Medical Diagnostics Assistant")
# api_url = "http://localhost:8000"
api_url = "https://ai-diagnosis-npob.onrender.com"
symptom_input = st.text_area("Describe your symptoms")

if st.button("Get Diagnosis"):
    state_input = {
        "input": symptom_input,
        "symptom_area": "",
        "diagnosis": ""
    }

    try:
        response = requests.post(
            f"{api_url}/diagnose/invoke",
            headers={"Content-Type": "application/json"},
            json={"input": state_input}  # ✅ Fix: Do not wrap in another "input"
        )

        data = response.json()
        st.write("DEBUG Raw JSON:", data)  # Optional

        output = data.get("output", {})

        st.subheader("Symptom Area Detected:")
        st.write(output.get("symptom_area", "N/A"))

        st.subheader("AI Diagnosis Suggestion:")
        st.write(output.get("diagnosis", "N/A"))

    except Exception as e:
        st.error(f"❌ Failed to get diagnosis: {e}")
