import streamlit as st
import requests

# ---------- Page Config ----------
st.set_page_config(
    page_title="Technology Service Dashboard",
    layout="centered",
    page_icon="🚀"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
    color: white;
}
.header-box {
    padding: 2rem;
    border-radius: 18px;
    background: linear-gradient(135deg, #6a11cb, #2575fc);
    box-shadow: 0px 10px 25px rgba(0,0,0,0.35);
    margin-bottom: 2rem;
}
.tool-card {
    background: #161b22;
    padding: 1.2rem;
    border-radius: 14px;
    margin-bottom: 0.8rem;
    border-left: 5px solid #2575fc;
    transition: transform 0.2s ease-in-out;
}
.tool-card:hover {
    transform: scale(1.02);
}
.badge {
    display: inline-block;
    padding: 0.25rem 0.6rem;
    border-radius: 8px;
    background-color: #2575fc;
    font-size: 0.75rem;
    margin-left: 0.5rem;
}
.footer {
    opacity: 0.6;
    font-size: 0.85rem;
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("""
<div class="header-box">
    <h1>🚀 Technology Service Dashboard</h1>
    <p>Explore available tools exposed by the backend API</p>
</div>
""", unsafe_allow_html=True)

# ---------- API ----------
api_url = "http://localhost:8000/technologies"

st.write("Click the button below to retrieve data from the backend service.")

# ---------- Action ----------
if st.button("🔄 Load Technologies", use_container_width=True):
    with st.spinner("Fetching technologies..."):
        try:
            api_response = requests.get(api_url, timeout=5)
            api_response.raise_for_status()
            payload = api_response.json()

            count = payload.get("count", 0)
            tools = payload.get("tools", [])

            st.success(f"✅ Received {count} technologies")

            if not tools:
                st.info("No technologies available at the moment.")
            else:
                for item in tools:
                    st.markdown(f"""
                    <div class="tool-card">
                        <strong>{item['name']}</strong>
                        <span class="badge">{item['type']}</span>
                    </div>
                    """, unsafe_allow_html=True)

        except requests.exceptions.RequestException as err:
            st.error("❌ Backend service is not reachable")
            st.caption(str(err))

# ---------- Footer ----------
st.markdown("""
<div class="footer">
    Powered by FastAPI · Streamlit · Python
</div>
""", unsafe_allow_html=True)

