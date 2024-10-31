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

with tab1:
    col1, col2, col3= st.columns([4,5,4])
    with col1:
        st.write('Install and Import')
        st.code("""$ pip install streamlit
import streamlit as st""")
        st.write('Run streamlit file')
        st.code("""streamlit run filename.py""")

        st.write('Learn about streamlit basic functions:')
                with st.expander("Text Elements"):
                    st.help(st.title)
                    st.help(st.header)
                    st.help(st.subheader)
                    st.help(st.text)
                    st.help(st.write)
                    st.help(st.markdown)
                    st.help(st.caption)
                    st.help(st.latex)
                    st.help(st.code)
            st.help(st.echo)
