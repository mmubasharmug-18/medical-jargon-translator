import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

MODEL = os.environ.get("GROQ_MODEL", "openai/gpt-oss-120b")
MAX_NOTE_CHARS = 4000
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30


def get_api_key():
    key = os.environ.get("GROQ_API_KEY")
    if not key or key == "your_key_here":
        try:
            import streamlit as st
            key = st.secrets["GROQ_API_KEY"]
        except Exception:
            key = None
    if not key or key == "your_key_here":
        raise RuntimeError("GROQ_API_KEY is not set. Add your key to the .env file.")
    return key
