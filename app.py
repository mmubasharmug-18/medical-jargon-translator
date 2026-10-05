import streamlit as st

from components.input_panel import render_input
from components.result_panel import render_result
from components.sidebar import render_sidebar
from src.llm_client import translate
from src.styles import apply_styles
from src.validation import validate_note

st.set_page_config(page_title="Medical Jargon Translator", page_icon="🩺", layout="wide")
apply_styles()

st.markdown("<h1 style='text-align:center;'>🩺 Medical Jargon Translator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Paste a clinical note and get a plain-language version below it.</p>",
            unsafe_allow_html=True)

st.session_state.setdefault("note", "")
st.session_state.setdefault("result", None)
st.session_state.setdefault("history", [])

settings = render_sidebar()
note, clicked = render_input()

if clicked:
    problem = validate_note(note)
    if problem:
        st.warning(problem)
    else:
        try:
            with st.spinner("Translating..."):
                result = {"note": note, "text": translate(note, settings)}
        except Exception as err:
            st.session_state.result = None
            st.error(str(err))
        else:
            st.session_state.result = result
            st.session_state.history.insert(0, result)
            del st.session_state.history[5:]
            st.rerun()

if st.session_state.result:
    render_result(st.session_state.result)