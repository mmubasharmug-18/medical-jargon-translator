import streamlit as st

from src.prompts import LANGUAGES
from src.samples import SAMPLES


def _load_sample():
    choice = st.session_state.sample
    if choice != "None":
        st.session_state.note = SAMPLES[choice]
        st.session_state.result = None


def _clear():
    st.session_state.note = ""
    st.session_state.result = None
    st.session_state.sample = "None"


def _open_history(i):
    item = st.session_state.history[i]
    st.session_state.note = item["note"]
    st.session_state.result = item


def render_sidebar():
    with st.sidebar:
        st.header("Settings")
        level = st.radio("Reading level", ["Simple", "Very simple"],
                         help="Very simple uses even shorter sentences.")
        language = st.selectbox("Output language", LANGUAGES)
        words = st.checkbox("Explain medical words", value=True)
        questions = st.checkbox("Add questions for my doctor", value=True)

        st.selectbox("Try a sample note", ["None"] + list(SAMPLES),
                     key="sample", on_change=_load_sample)
        st.button("Clear note", on_click=_clear)

        st.subheader("Recent translations")
        history = st.session_state.get("history", [])
        if not history:
            st.caption("Nothing yet. Your last 5 translations will show here.")
        for i, item in enumerate(history):
            short = item["note"][:26] + ("..." if len(item["note"]) > 26 else "")
            st.button(f"{i + 1}. {short}", key=f"hist_{i}", on_click=_open_history, args=(i,))

    return {"level": level, "language": language, "words": words, "questions": questions}