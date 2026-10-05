import streamlit as st


def render_result(result):
    st.subheader("Original note")
    with st.container(border=True):
        st.text(result["note"])

    st.subheader("Plain language")
    with st.container(border=True):
        st.markdown(result["text"])

    download_text = f"ORIGINAL NOTE\n{result['note']}\n\nPLAIN LANGUAGE\n{result['text']}\n"
    st.download_button("Download translation (.txt)", data=download_text, file_name="translation.txt")

    st.caption("This is an AI translation to help you understand your note. "
               "It is not medical advice. Talk to your doctor about your health.")