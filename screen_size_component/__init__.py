import streamlit.components.v1 as components
import os

absolute_path = os.path.dirname(os.path.abspath(__file__))
frontend_path = absolute_path

streamlit_js_eval = components.declare_component(
    "streamlit_js_eval",
    path=frontend_path
)

def get_screen_size(component_key=None):
    js_text = 'getScreenSize()' #'getScreenSize()' is a javascript function present in index.html file which returns the size of user's browser
    if component_key is None: component_key = js_text
    size_json = streamlit_js_eval(js_expressions=js_text, key=component_key)
    return size_json