import streamlit as st
import time
import pandas as pd
import numpy as np
import random
import annotated_text 
from streamlit_card import card 
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from annotated_text import annotation
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.buy_me_a_coffee import button

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
listTabs = ["Streamlit Basic Functions", "Streamlit Elements", "Personality Test Project"]
tab1, tab2, tab3= st.tabs(listTabs)
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

        if on5:
            placeholder2.write("This will be executed")
            st.stop()
            placeholder32.write("This will not be executed")

        else:
            st.code("""st.write("This will be executed")
st.stop()
st.write("This will not be executed")""")
        base_html6 = """
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

        st.write('Input Widgets')
        on6 = st.toggle("Activate features", key = 'nn5')

        placeholder2 = st.empty()
        placeholder22 = st.empty()
        placeholder32 = st.empty()
        placeholder42 = st.empty()
        placeholder52 = st.empty()
        placeholder62 = st.empty()
        placeholder72 = st.empty()
        placeholder82 = st.empty()
        placeholder92 = st.empty()

        if on6:
            placeholder2.button("Click me", type='primary')
            placeholder22.download_button("Download", data="Hello, World!", file_name="hello.txt", type='secondary')
            placeholder32.checkbox("I agree")
            placeholder42.radio("Pick one", ["Option 1", "Option 2"])
            placeholder52.selectbox("Pick one", ["Option A", "Option B"])
            placeholder62.multiselect("Choose", ["Option 1", "Option 2", "Option 3"])
            placeholder72.slider("Slide me", 0, 100)
            placeholder82.select_slider("Pick one", options=["bad", "good", "excellent"])
            placeholder92.color_picker("Pick a color")
            st.toggle('Toggle')
            picture = st.camera_input("Take a picture")
            if picture:
                st.image(picture)
            st.link_button("Go to Google.com", "https://google.com")

        else:
            st.code("""st.button("Click me")
st.download_button("Download", data="Hello, World!", file_name="hello.txt")
st.checkbox("I agree")
st.radio("Pick one", ["Option 1", "Option 2"])
st.selectbox("Pick one", ["Option A", "Option B"])
st.multiselect("Choose", ["Option 1", "Option 2", "Option 3"])
st.slider("Slide me", 0, 100)
st.select_slider("Pick one", options=["bad", "good", "excellent"])
st.color_picker("Pick a color")
st.toggle('Toggle')
picture = st.camera_input("Take a picture")
if picture:
st.image(picture)
st.link_button("Go to Google.com", "https://google.com")""")

        base_html7 = """
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

        on7 = st.toggle("Activate features", key = 'nn6')

        placeholder2 = st.empty()
        placeholder22 = st.empty()
        placeholder32 = st.empty()
        placeholder42 = st.empty()
        placeholder52 = st.empty()
        placeholder62 = st.empty()

        if on7:
            placeholder2.text_input("Enter some text")
            placeholder22.number_input("Enter a number", min_value=0, max_value=10)
            placeholder32.text_area("Enter a description")
            placeholder42.date_input("Pick a date")
            placeholder52.time_input("Pick a time")
            placeholder62.file_uploader("Upload a file")

        else:
            st.code("""st.text_input("Enter some text")
st.number_input("Enter a number", min_value=0, max_value=10)
st.text_area("Enter a description")
st.date_input("Pick a date")
st.time_input("Pick a time")
st.file_uploader("Upload a file")""")
        base_html8 = """
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

        st.write('Layout and Containers')
        on8 = st.toggle("Activate features", key = 'nn7')

        placeholder2 = st.empty()
        placeholder22 = st.empty()
        placeholder32 = st.empty()

        if on8:
            with placeholder2.container():
                placeholder2.write("This is inside a container")

            col1, col2 = placeholder22.columns(2)
            col1.write("This is column 1")
            col2.write("This is column 2")

            with st.expander("Expand me"):
                st.write("This is hidden text")
            
            with st.popover('Popover'):
                st.write("This is hidden text")

        else:
            st.code("""with st.container():
st.write("This is inside a container")

col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")

with st.expander("Expand me"):
st.write("This is hidden text")
                
with st.popover('Popover'):
st.write("This is hidden text")""")
            
        st.write('Media Elements')
        on12 = st.toggle("Activate features", key = 'nn11')
        if on12:
            from PIL import Image

            image = Image.open(r"C:\Users\nasreenn\Desktop\azure-open-ai-embeddings-qna\code\pages\streamlit-logo.png")
            st.image(image, caption="Streamlit Logo")

            # st.audio("path_to_audio.mp3")
            # st.video("path_to_video.mp4")
        else: 
            st.code("""image = Image.open("path_to_image.jpg")
st.image(image, caption="Streamlit Logo")

st.audio("path_to_audio.mp3")
st.video("path_to_video.mp4")""")
            
        st.write('Session Elements')
        on13 = st.toggle("Activate features", key = 'nn12')
        if on13:
            if 'counter' not in st.session_state:
                st.session_state.counter = 0

            def increment_counter():
                st.session_state.counter += 1

            st.write("Counter:", st.session_state.counter)
            st.button("Increment", on_click=increment_counter, type='primary')
        else: 
            st.code("""if 'counter' not in st.session_state:
st.session_state.counter = 0

def increment_counter():
st.session_state.counter += 1

st.write("Counter:", st.session_state.counter)
st.button("Increment", on_click=increment_counter)""")
            
    with col3:
        st.write('Streamlit Basic Functions')

        st.write('Data Display Elements')
        on9 = st.toggle("Activate features", key = 'nn8')
        if on9:
            df = pd.DataFrame({
                'Col1': [1, 2, 3, 4],
                'Col2': [10, 20, 30, 40]
            })

            st.dataframe(df)
            st.data_editor(df, num_rows='dynamic')
            st.table(df)
            st.json({'key': 'value', 'key2': [1, 2, 3]})
            st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

        else:
            st.code("""df = pd.DataFrame({
'Col1': [1, 2, 3, 4],
'Col2': [10, 20, 30, 40]
})

st.dataframe(df)
st.data_editor(df, num_rows='dynamic')
st.table(df)
st.json({'key': 'value', 'key2': [1, 2, 3]})
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
""")
            st.write('Charts')
            on10 = st.toggle("Activate features", key = 'nn9')
            if on10:
                chart_data = pd.DataFrame(
                    np.random.randn(20, 3),
                    columns=['a', 'b', 'c']
                )

                st.line_chart(chart_data)
                st.area_chart(chart_data)
                st.bar_chart(chart_data)

                # Altair
                c = alt.Chart(chart_data).mark_circle().encode(
                    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
                )
                st.altair_chart(c)

                # Matplotlib
                fig, ax = plt.subplots()
                ax.scatter(chart_data['a'], chart_data['b'])
                st.pyplot(fig)

                # Plotly
                fig = px.scatter(chart_data, x='a', y='b', color='c')
                st.plotly_chart(fig)

                # Bokeh
                from bokeh.plotting import figure
                from bokeh.io import output_file, show

                p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
                p.line(chart_data.index, chart_data['a'], legend_label="Temp.", line_width=2)
                st.bokeh_chart(p)

                # Pydeck
                import pydeck as pdk

                layer = pdk.Layer(
                    'ScatterplotLayer',
                    chart_data,
                    get_position='[a, b]',
                    get_radius=100,
                    get_color='[200, 30, 0, 160]',
                )
                view_state = pdk.ViewState(
                    latitude=0,
                    longitude=0,
                    zoom=1,
                    pitch=50,
                )
                st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

                # Map
                map_data = pd.DataFrame(
                    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
                    columns=['lat', 'lon']
                )
                st.map(map_data)
            else:
                st.code("""chart_data = pd.DataFrame(
np.random.randn(20, 3),
columns=['a', 'b', 'c']
)

st.line_chart(chart_data)
st.area_chart(chart_data)
st.bar_chart(chart_data)

# Altair
c = alt.Chart(chart_data).mark_circle().encode(
x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)
st.altair_chart(c)

# Matplotlib
fig, ax = plt.subplots()
ax.scatter(chart_data['a'], chart_data['b'])
st.pyplot(fig)

# Plotly
fig = px.scatter(chart_data, x='a', y='b', size='c', color='c')
st.plotly_chart(fig)

# Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
p.line(chart_data.index, chart_data['a'], legend_label="Temp.", line_width=2)
st.bokeh_chart(p)

# Pydeck
import pydeck as pdk

layer = pdk.Layer(
'ScatterplotLayer',
chart_data,
get_position='[a, b]',
get_radius=100,
get_color='[200, 30, 0, 160]',
)
view_state = pdk.ViewState(
latitude=0,
longitude=0,
zoom=1,
pitch=50,
)
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

# Map
map_data = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
columns=['lat', 'lon']
)
st.map(map_data)""")
            
            st.write('Caching')
            on11 = st.toggle("Activate features", key = '10')
            if on11: 
                @st.cache_data
                def load_data():
                    time.sleep(3)
                    return {"data": "sample"}

                data = load_data()
                st.write(data)

                @st.cache_resource
                def expensive_computation(x):
                    time.sleep(3)
                    return x * x

                result = expensive_computation(10)
                st.write(result)  
            else: 
                st.code("""@st.cache_data
def load_data():
time.sleep(3)
return {"data": "sample"}

data = load_data()
st.write(data)

@st.cache_resource
def expensive_computation(x):
time.sleep(3)
return x * x

result = expensive_computation(10)
st.write(result) """)
            
            st.write('Layout and Containers')
            on14 = st.toggle("Activate features", key = '13')
            if on14:
                Section1, Section2, Section3 = st.tabs(["Section1", "Section2", "Section3"])

                with Section1:
                    st.header("Section1")

                with Section2:
                    st.header("Section2")

                with Section3:
                    st.header("Section3")
            else: 
                st.code("""Section1, Section2, Section3 = st.tabs(["Section1", "Section2", "Section3"])

with Section1:
st.header("Section1")

with Section2:
st.header("Section2")

with Section3:
st.header("Section3")""")
            
            on16 = st.toggle("Activate features", key = '15')
            if on16:
                with st.form("my_form"):
                    slider_val = st.slider("Form slider")
                    checkbox_val = st.checkbox("Form checkbox")

                    submitted = st.form_submit_button("Submit")
                    if submitted:
                        st.write("slider", slider_val, "checkbox", checkbox_val)
            else: 
                st.code("""with st.form("my_form"):
slider_val = st.slider("Form slider")
checkbox_val = st.checkbox("Form checkbox")

submitted = st.form_submit_button("Submit")
if submitted:
    st.write("slider", slider_val, "checkbox", checkbox_val)""")

            st.write('Database')  
            st.code("""
                    st_conn = st.connection("sql")    
                    
                    conn = st.connection("my_sql_connection", type="streamlit.connections.SQLConnection")
                    
                    from streamlit.connections import SQLConnection
                    conn = st.connection("my_sql_connection", type=SQLConnection).""")
        
## Designs
with tab2:
    col1, col2, col3 = st.columns(3)
    with col1:
        x1 = st.toggle("See code", key = 'x1')
        if x1:
            with st.echo():
                with stylable_container(
                    key="click",
                    css_styles="""
                    button{
                    background-color: #00b090;
                    font-weight: bold;
                    color: white;
                    }
                    """,
        
                
                ):
                    st.button("Click Me", key="click")
        else: 
            with stylable_container(
                key="click",
                css_styles="""
                button{
                background-color: #00b090;
                font-weight: bold;
                color: white;
                }
                """,
    
            
            ):
                st.button("Click Me", key="click")
        
        x2 = st.toggle("See code", key = 'x2')
        if x2:
            with st.echo():
                with stylable_container(
                    key="upload_file",
                    css_styles="""
                    button {
                    background-color: #daae66;
                    color: white;
                    }
                    div[data-testid="stFileUploader"]{
                    }
                    [data-testid='stFileUploader'] {
                    width: max-content;
                }
                [data-testid='stFileUploader'] section {
                    padding: 0;
                    float: left;
                }
                [data-testid='stFileUploader'] section > input + div {
                    display: none;
                }
                [data-testid='stFileUploader'] section + div {
                    margin-top: 10%;
                }
                    """,
                
                ):
                    st.file_uploader("", type=['pdf', 'txt', 'docx'], accept_multiple_files=True)
        else:
            with stylable_container(
                    key="upload_file",
                    css_styles="""
                    button {
                    background-color: #daae66;
                    color: white;
                    }
                    div[data-testid="stFileUploader"]{
                    }
                    [data-testid='stFileUploader'] {
                    width: max-content;
                }
                [data-testid='stFileUploader'] section {
                    padding: 0;
                    float: left;
                }
                [data-testid='stFileUploader'] section > input + div {
                    display: none;
                }
                [data-testid='stFileUploader'] section + div {
                    margin-top: 10%;
                }
                    """,
                
                ):
                    st.file_uploader("", type=['pdf', 'txt', 'docx'], accept_multiple_files=True)

        x3 = st.toggle("See code", key = 'x3')
        if x3:
            with st.echo():
                with stylable_container(
                key="text_input",
                css_styles="""
                div[data-testid="stTextInput"]{
                width: 60%;
                }
                """,
            
                ):
                    st.text_input("", placeholder="Type your message...")
        else: 
            with stylable_container(
                key="text_input",
                css_styles="""
                div[data-testid="stTextInput"]{
                width: 60%;
                }
                """,
            
            ):
                st.text_input("", placeholder="Type your message...")

        x4 = st.toggle("See code", key = 'x4')
        if x4:
            with st.echo():
                st.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css"/>', unsafe_allow_html=True)
                st.markdown(
                    f"""
                        <p>Use Font Awesome Icons</p>
                        <i class="fas fa-user" style="color:blue;"></i>
                        <i class="fa fa-car" style="color:red;"></i>
                        <i class="fa fa-spinner fa-spin" style="color:green;"></i>
                        <i class="fa fa-circle-o-notch fa-spin" style="color:pink;"></i>
                        <i class="fa fa-refresh fa-spin" style="color:brown;"></i>
                        <i class="fa fa-cog fa-spin" style="color:yellow;"></i>
                        <i class="fa fa-spinner fa-pulse"></i>
                    """,
                    unsafe_allow_html=True
            )
        else: 
            st.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css"/>', unsafe_allow_html=True)
            st.markdown(
            f"""
                <p>Use Font Awesome Icons</p>
                <i class="fas fa-user" style="color:blue;"></i>
                <i class="fa fa-car" style="color:red;"></i>
                <i class="fa fa-spinner fa-spin" style="color:green;"></i>
                <i class="fa fa-circle-o-notch fa-spin" style="color:pink;"></i>
                <i class="fa fa-refresh fa-spin" style="color:brown;"></i>
                <i class="fa fa-cog fa-spin" style="color:yellow;"></i>
                <i class="fa fa-spinner fa-pulse"></i>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.write('Feedback Form:')
        x5 = st.toggle("See code", key = 'x5')
        if x5:
            with st.echo():
                with stylable_container(
                    key="Feedback",
                    css_styles="""
                    button {
                    background-color: #9000f7;
                    color: white;
                }
                div[data-testid="stPopover"]{
                    font-weight: bold;
                    border-radius: 5px;
                    white-space: nowrap;
                }
                """
                ):
                    with st.popover('Feedback'):
                        with st.form(key='feedback_form', clear_on_submit =True):
                                st.header(body="Feedback Form!")
                                st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
                                overall_experience = st.radio('Overall Experience', ['😃', '🙂','😐','😕','😞'])
                                feedback_options = st.multiselect("Feedback On Tabs:",["Basics", "Designs", "Application"])
                                feedback_comment = st.text_input('Feedback Comment')
                                submitted = st.form_submit_button('Submit', type = 'primary')
        else: 
            with stylable_container(
                key="Feedback",
                css_styles="""
                button {
                background-color: #9000f7;
                color: white;
            }
             div[data-testid="stPopover"]{
                font-weight: bold;
                border-radius: 5px;
                white-space: nowrap;
            }
            """
            ):
                with st.popover('Feedback'):
                    with st.form(key='feedback_form', clear_on_submit =True):
                            st.header(body="Feedback Form!")
                            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
                            overall_experience = st.radio('Overall Experience', ['😃', '🙂','😐','😕','😞'])
                            feedback_options = st.multiselect("Feedback On Tabs:",["Basics", "Designs", "Application"])
                            feedback_comment = st.text_input('Feedback Comment')
                            submitted = st.form_submit_button('Submit', type = 'primary')

        st.write('Dataframe:')
        x6 = st.toggle("See code", key = 'x6')
        if x6:
            with st.echo():
                @st.cache_data
                def add_empty_row(df, index):
                    empty_row = pd.DataFrame([[False, False, '', '']], columns=df.columns)
                    return pd.concat([df.iloc[:index], empty_row, df.iloc[index:]]).reset_index(drop=True)

                @st.cache_data
                def delete_row(df, index):
                    return df.drop(index).reset_index(drop=True)

                df = pd.DataFrame({
                        '➕': [False] * 4,
                        '➖': [False] * 4,
                        'Col1': ['1', '2', '3', '4'],
                        'Col2': ['10', '20', '30', '40']
                    })
                if 'state_df' not in st.session_state:
                    st.session_state.state_df = df.copy()

                df = st.session_state.state_df

                df = st.data_editor(df, column_config={
                            "➕": st.column_config.CheckboxColumn(
                            "➕",
                            help="Add Row",
                            default=False,
                            ),
                            "➖": st.column_config.CheckboxColumn(
                            "➖",
                            help="Remove Row",
                            default=False,
                            )}, num_rows='fixed', hide_index=True)

                df1 = df.copy()

                for index, row in df.iterrows():
                    if row['➕'] == True:
                        st.session_state.state_df = df1
                        st.session_state.state_df.at[index, '➕'] = False
                        st.session_state.state_df = add_empty_row(st.session_state.state_df, index)
                        st.rerun()

                for index, row in df.iterrows():
                    if row['➖'] == True:
                        st.session_state.state_df = df1
                        st.session_state.state_df.at[index, '➖'] = False
                        st.session_state.state_df = delete_row(st.session_state.state_df, index)
                        st.rerun()
        else: 
            @st.cache_data
            def add_empty_row(df, index):
                empty_row = pd.DataFrame([[False, False, '', '']], columns=df.columns)
                return pd.concat([df.iloc[:index], empty_row, df.iloc[index:]]).reset_index(drop=True)

            @st.cache_data
            def delete_row(df, index):
                return df.drop(index).reset_index(drop=True)

            df = pd.DataFrame({
                    '➕': [False] * 4,
                    '➖': [False] * 4,
                    'Col1': ['1', '2', '3', '4'],
                    'Col2': ['10', '20', '30', '40']
                })
            if 'state_df' not in st.session_state:
                st.session_state.state_df = df.copy()

            df = st.session_state.state_df

            df = st.data_editor(df, column_config={
                        "➕": st.column_config.CheckboxColumn(
                        "➕",
                        help="Add Row",
                        default=False,
                        ),
                        "➖": st.column_config.CheckboxColumn(
                        "➖",
                        help="Remove Row",
                        default=False,
                        )}, num_rows='fixed', hide_index=True)

            df1 = df.copy()

            for index, row in df.iterrows():
                if row['➕'] == True:
                    st.session_state.state_df = df1
                    st.session_state.state_df.at[index, '➕'] = False
                    st.session_state.state_df = add_empty_row(st.session_state.state_df, index)
                    st.rerun()

            for index, row in df.iterrows():
                if row['➖'] == True:
                    st.session_state.state_df = df1
                    st.session_state.state_df.at[index, '➖'] = False
                    st.session_state.state_df = delete_row(st.session_state.state_df, index)
                    st.rerun()
        st.write('Annotation:')
        x7 = st.toggle("See code", key = 'x7')
        if x7:
            with st.echo():
                annotated_text.annotated_text( 
                annotation("Streamlit", color='#07a631'), 
                ("is", "so", 'lightblue'),   
                    
                annotation("COOL", border='3px groove yellow'), 
            ) 
        else: 
            annotated_text.annotated_text( 
            annotation("Streamlit", color='#07a631'), 
            ("is", "so", 'lightblue'),   
                
            annotation("COOL", border='3px groove yellow'), 
        ) 
    with col3:
        st.write('Card:')
        x8 = st.toggle("See code", key = 'x8')
        if x8:  
            with st.echo():  
                card( 
                title="Hello Users!", 
                text="Click this card to redirect to Streamlit", 
                image="https://raw.githubusercontent.com/Nargis99/iPlan/main/streamlit-logo.png", 
                url="https://streamlit.io/", 
            ) 
        else: 
                    card( 
                        title="Hello Users!", 
                        text="Click this card to redirect to Streamlit", 
                        image="https://raw.githubusercontent.com/Nargis99/iPlan/main/streamlit-logo.png", 
                        url="https://streamlit.io/", 
                        styles={
                            "card": {
                                "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
                                "height": "300px" # <- if you want to set the card height to 300px
                            }
                        }
                    )
with tab3:
    # Define questions and options
    questions = [
        "How do you feel in large social gatherings?",
        "Do you prefer to spend your free time alone?",
        "How do you react when meeting new people?",
        "What energizes you the most?",
        "How do you feel after spending a day alone?",
        "Do you often seek out social events?",
        "Do you enjoy deep conversations with a few people?",
        "Do you feel drained after socializing for long periods?",
    ]
    
    options = [
        ["Excited 😄", "Neutral 😐", "Overwhelmed 😰"],  # Q1
        ["Yes 🙋‍♂️", "Sometimes 🤔", "No 🙅‍♂️"],         # Q2
        ["I love it! 🎉", "I'm okay with it 🤷‍♂️", "I prefer to avoid it 🚫"],  # Q3
        ["Socializing 🥳", "Reading 📚", "Both ⚖️"],      # Q4
        ["Refreshed 🌟", "Neutral 😌", "Drained 😩"],       # Q5
        ["Always 🙌", "Occasionally 🤗", "Rarely 🙈"],     # Q6
        ["Absolutely 💯", "Depends 🤷", "Not really 🙁"],  # Q7
        ["Yes 😥", "Sometimes 🤷‍♀️", "No 👍"],            # Q8
    ]
    
    # Scoring for each personality type
    scores = {
        "Extrovert": 0,
        "Introvert": 0,
        "Ambivert": 0,
    }
    
    # Define scoring based on responses
    def calculate_scores(responses):
        for response in responses:
            if response in ["Excited 😄", "I love it! 🎉", "Socializing 🥳", "Refreshed 🌟", "Always 🙌", "Absolutely 💯"]:
                scores["Extrovert"] += 1
            elif response in ["Neutral 😐", "Sometimes 🤔", "I'm okay with it 🤷‍♂️", "Both ⚖️", "Neutral 😌", "Occasionally 🤗", "Depends 🤷‍♀️", "Sometimes 🤷‍♀️"]:
                scores["Ambivert"] += 1
            else:
                scores["Introvert"] += 1
    
    # Streamlit app layout
    st.title("🌟 Personality Quiz: Are You an Extrovert, Introvert, or Ambivert?🌟")
    st.header("Answer the following questions:")
    
    responses = []
    for i, question in enumerate(questions):
        response = st.radio(question, options[i], key=i)
        responses.append(response)
    
    # Submit button
    if st.button("Submit"):
        calculate_scores(responses)
        # Determine personality type
        personality_type = max(scores, key=scores.get)
        
        # Show result with emojis
        if personality_type == "Extrovert":
            emoji = "🎉"
        elif personality_type == "Introvert":
            emoji = "🌙"
        else:
            emoji = "⚖️"
        
        st.success(f"Your personality type is: **{personality_type}** {emoji}")
        st.subheader("Scores breakdown:")
        fig = go.Figure(data=[
        go.Bar(
            x=list(scores.keys()),
            y=list(scores.values()),
            marker_color=['#FF9999', '#66B3FF', '#99FF99'],
            text=list(scores.values()),
            textposition='auto'
        )
    ])
    
        fig.update_layout(
            title="Personality Type Scores",
            xaxis_title="Personality Type",
            yaxis_title="Scores",
            plot_bgcolor='rgba(0,0,0,0)',  # Transparent plot background
            paper_bgcolor='rgba(0,0,0,0)',  # Transparent paper background
            title_x=0.5,  # Center the title
            height=400,
            width=600,
            margin=dict(l=40, r=40, t=40, b=40)
        )
    
        st.plotly_chart(fig, use_container_width=True)

    
        # Additional insights
        st.subheader("Insights:")
        if personality_type == "Extrovert":
            st.write("You thrive in social situations and enjoy being around people!")
        elif personality_type == "Introvert":
            st.write("You prefer solitude or small gatherings and enjoy deep conversations.")
        else:
            st.write("You have a balance of both traits, adapting to different situations.")
        time.sleep(4)
        st.toast('You can try again🤗')



footer="""<style>
.footer {
left: 0;
bottom: 0;
width: 100%;
color: black;
text-align: center;
z-index: 1;
}

</style>
<div class="footer">
<p style="font-size: 12px; ">Made with ❤️ by Nargis Nasreen</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

# button(username="sheet", floating=False, width=250)
