import streamlit as st

CSS = """
<style>
/* ---------- main page: white background, black text ---------- */
.stApp, [data-testid="stHeader"] { background: #ffffff !important; }
.stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp li,
.stApp label, .stApp span, [data-testid="stText"] { color: #000000 !important; }

textarea { background: #f4f6fb !important; color: #000000 !important; }
div[data-baseweb="textarea"], div[data-baseweb="base-input"] { background: #f4f6fb !important; }

/* ---------- sidebar: gradient from the colour image ---------- */
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div,
[data-testid="stSidebar"] > div > div {
    background: linear-gradient(90deg, #2db5d3 0%, #6a5ac8 100%) fixed !important;
}
[data-testid="stSidebar"] { min-height: 100vh; }
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] *,
[data-testid="stSidebar"] [data-testid="stRadio"] label *,
[data-testid="stSidebar"] [data-testid="stCheckbox"] label *,
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] * { color: #ffffff !important; }

[data-testid="stSidebar"] div[data-baseweb="select"] > div { background: #ffffff !important; }
[data-testid="stSidebar"] div[data-baseweb="select"] * { color: #000000 !important; }

/* ---------- warning box and buttons ---------- */
.stApp [data-testid="stAlert"] { background: #fff4d6 !important; }
.stApp [data-testid="stAlert"] * { color: #5c4300 !important; }

.stApp .stButton button,
.stApp .stDownloadButton button { background: #5a63c8 !important; border: none !important; }
.stApp .stButton button, .stApp .stButton button *,
.stApp .stDownloadButton button, .stApp .stDownloadButton button * { color: #ffffff !important; }

/* sidebar buttons: white so they show up on the gradient */
[data-testid="stSidebar"] .stButton button { background: #ffffff !important; }
[data-testid="stSidebar"] .stButton button,
[data-testid="stSidebar"] .stButton button * { color: #2b2f6b !important; }
</style>
"""


def apply_styles():
    st.markdown(CSS, unsafe_allow_html=True)