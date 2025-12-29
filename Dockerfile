# Use python image
FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Expose ports for both FastAPI (8000) and Streamlit (8501)
EXPOSE 8000 8501

# Command to run both (simplified for this example)
CMD uvicorn app_api:app --host 0.0.0.0 --port 8000 & streamlit run app_ui.py --server.port 8501 --server.address 0.0.0.0