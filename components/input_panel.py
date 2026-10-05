import streamlit as st

from src.config import MAX_NOTE_CHARS


def render_input():
    note = st.text_area("Clinical note", key="note", height=220,
                        placeholder="e.g. 58 y/o M c/o SOB x2 days. Hx of HTN...")
    st.caption(f"{len(note)} / {MAX_NOTE_CHARS} characters")
    clicked = st.button("Translate", type="primary")
    return note, clicked
