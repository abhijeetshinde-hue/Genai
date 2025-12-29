import streamlit as st
import requests

st.set_page_config(page_title="API Viewer", layout="centered")
st.header("Technology Service Dashboard")

api_url = "http://localhost:8000/technologies"

st.write("Click the button below to retrieve data from the backend service.")

if st.button("Load Technologies"):
    try:
        api_response = requests.get(api_url, timeout=5)
        api_response.raise_for_status()

        payload = api_response.json()
        st.success(f"Received {payload.get('count', 0)} records")

        for item in payload.get("tools", []):
            st.markdown(f"- **{item['name']}** ({item['type']})")

    except requests.exceptions.RequestException as err:
        st.error("Backend service is not reachable")
        st.caption(str(err))
