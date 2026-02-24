import streamlit as st
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.set_page_config(page_title="AI Knowledge Assistant")

st.title("AI Knowledge Assistant")

question = st.text_input("Ask a question")

if st.button("Ask"):
    if question:
        response = requests.post(
            f"{BACKEND_URL}/ask",
            json={"question": question}
        )
        st.write(response.json()["answer"])
