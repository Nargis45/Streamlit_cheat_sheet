import streamlit as st

st.set_page_config(layout="wide")

st.title("All about Streamlit :coffee: ")
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #ffefba, #ffffff);
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)
#tabs
listTabs = ["Cheat Sheet", "Designs"]
tab1, tab2= st.tabs(listTabs)


