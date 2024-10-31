import streamlit as st
import time

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

        with st.expander("Status Elements"):
            st.help(st.success)
            st.help(st.info)
            st.help(st.warning)
            st.help(st.error)
            st.help(st.balloons)
            st.help(st.snow)
            st.help(st.progress)
            st.help(st.toast) 
            st.help(st.spinner)
            st.help(st.exception)
            st.help(st.status)
            st.help(st.divider)

        with st.expander("Control Flow"):
            st.help(st.stop)

        with st.expander("Input Widgets"):
            st.help(st.button)
            st.help(st.download_button)
            st.help(st.checkbox)
            st.help(st.radio)
            st.help(st.selectbox)
            st.help(st.multiselect)
            st.help(st.slider)
            st.help(st.select_slider)
            st.help(st.color_picker)
            st.help(st.toggle)
            st.help(st.camera_input)
            st.help(st.image)
            st.help(st.link_button)
            st.help(st.text_input)
            st.help(st.number_input)
            st.help(st.text_area)
            st.help(st.date_input)
            st.help(st.time_input)
            st.help(st.file_uploader)

        with st.expander("Layouts and Containers"):
            st.help(st.container)
            st.help(st.columns)
            st.help(st.expander)
            st.help(st.popover)
            st.help(st.tabs)
            st.help(st.form)

        with st.expander("Media Elements"):
            st.help(st.image)
            st.help(st.audio)
            st.help(st.video)
            
        with st.expander("Session Elements"):
            st.help(st.session_state)
            
        with st.expander("Data Display Elements"):
            st.help(st.dataframe)
            st.help(st.data_editor)
            st.help(st.table)
            st.help(st.json)
            st.help(st.metric)
            
        with st.expander("Charts Elements"):
            st.help(st.line_chart)
            st.help(st.area_chart)
            st.help(st.bar_chart)
            st.help(st.altair_chart)
            st.help(st.pyplot)
            st.help(st.plotly_chart)
            st.help(st.bokeh_chart)
            st.help(st.pydeck_chart)
            st.help(st.map)
        
        with st.expander("Caching"):
            st.help(st.cache_data)
            st.help(st.cache_resource)

        with st.expander("Database Connection"):
            st.help(st.cache_data)

    with col2:
        st.write('Streamlit Basic Functions')
        st.write('Text Elements')

        base_html = """
        <div style='color:black; background-color: #f2c5f2; font-size: 14px; padding: 14px; border-radius: 5px; margin-top:0; align: center; text-align: center;'>
            <style>
            .stApp {{
                background: linear-gradient(to right, #ff7e5f, #feb47b);
                color: white;
            }}
            </style>
            {}
        </div>
        """

        on = st.toggle("Activate features")
        placeholder = st.empty()
        placeholder2 = st.empty()
        placeholder3 = st.empty()
        placeholder4 = st.empty()
        placeholder5 = st.empty()

        if on:
            placeholder.title("Hello Streamlit!!")
            placeholder2.header('This is a header')
            placeholder3.subheader('This is a subheader')
            placeholder4.text('This is a text')
            placeholder5.write('This is a text using st.write')
        else:
            st.code("""st.title("Hello Streamlit!!")
st.header('This is a header')
st.subheader('This is a subheader')
st.text('This is a text')
st.write('This is a text using st.write')""")
            
        base_html3 = """
        <div style='color:black; background-color: #f2c5f2; font-size: 14px; padding: 14px; border-radius: 5px; margin-top:0; align: center; text-align: center;'>
            <style>
            .stApp {{
                background: linear-gradient(to right, #ff7e5f, #feb47b);
                color: white;
            }}
            </style>
            {}
        </div>
        """

        on3 = st.toggle("Activate features", key = 'nn2')

        placeholder2 = st.empty()
        placeholder22 = st.empty()
        placeholder32 = st.empty()
        placeholder42 = st.empty()

        if on3:
            placeholder2.markdown('*This* is **a** ***Markdown***')
            placeholder22.caption('This is a caption')
            placeholder32.latex(r'e^{i\pi} + 1 = 0')
            placeholder42.code("print('Hello, Streamlit!')")
            with st.echo():
                st.write('Hello, Streamlit!')

        else:
            st.code("""st.markdown('*This* is **a** ***Markdown***')
st.caption('This is a caption')
st.latex(r'e^{i\pi} + 1 = 0')
st.code("print('Hello, Streamlit!')")
with st.echo():
    st.write('Hello, Streamlit!')""")
            
            base_html2 = """
        <div style='color:black; background-color: #f2c5f2; font-size: 14px; padding: 14px; border-radius: 5px; margin-top:0; align: center; text-align: center;'>
            <style>
            .stApp {{
                background: linear-gradient(to right, #ff7e5f, #feb47b);
                color: white;
            }}
            </style>
            {}
        </div>
        """
        st.write('Status Elements')
        on2 = st.toggle("Activate features", key = 'nn')

        placeholder2 = st.empty()
        placeholder22 = st.empty()
        placeholder32 = st.empty()
        placeholder42 = st.empty()

        if on2:
            placeholder2.success("Success")
            placeholder22.info('Information')
            placeholder32.warning('Warning')
            placeholder42.error('Error')
        else:
            st.code("""st.success("Success")
st.info('Information')
st.warning('Warning')
st.error('Error')""")
            
        base_html4 = """
        <div style='color:black; background-color: #f2c5f2; font-size: 14px; padding: 14px; border-radius: 5px; margin-top:0; align: center; text-align: center;'>
            <style>
            .stApp {{
                background: linear-gradient(to right, #ff7e5f, #feb47b);
                color: white;
            }}
            </style>
            {}
        </div>
        """

        on4 = st.toggle("Activate features", key = 'nn3')

        placeholder2 = st.empty()
        placeholder22 = st.empty()
        placeholder32 = st.empty()

        if on4:
            placeholder2.balloons()
            placeholder22.snow()
            bar = placeholder32.progress(50)
            time.sleep(3)
            bar.progress(100)
            st.toast('I am here...')
            with st.spinner("Loading..."):
                time.sleep(6)
            try:
                1 / 0
            except ZeroDivisionError as e:
                placeholder42.exception(e)

        else:
            st.code("""st.balloons()
st.snow()
                    
bar = st.progress(50)
time.sleep(3)
bar.progress(100)
                    
st.toast('I am here...')
                    
with st.spinner("Loading..."):
    time.sleep(6)
                    
try:
    1 / 0
except ZeroDivisionError as e:
    st.exception(e)""")
        base_html5 = """
        <div style='color:black; background-color: #f2c5f2; font-size: 14px; padding: 14px; border-radius: 5px; margin-top:0; align: center; text-align: center;'>
            <style>
            .stApp {{
                background: linear-gradient(to right, #ff7e5f, #feb47b);
                color: white;
            }}
            </style>
            {}
        </div>
        """
        on15 = st.toggle("Activate features", key = '14')
        if on15:
            with st.status("Downloading data..."):
                st.write("Searching for data...")
                time.sleep(2)
                st.write("Found URL.")
                time.sleep(1)
                st.write("Data Downloaded.")
                time.sleep(1)
        else: 
            st.code("""with st.status("Downloading data..."):
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)""")

        togg = st.toggle("Activate features", key = 'togg')
        if togg:
            st.write('This is a text above divider')
            st.divider()
            st.write('This is  a text below divider')
        else: 
            st.code("""st.write('This is a text above divider')
st.divider()
st.write('This is  a text below divider')""")

        st.write('Control Flow')
        on5 = st.toggle("Activate features", key = 'nn4')

        placeholder2 = st.empty()
        placeholder32 = st.empty()
