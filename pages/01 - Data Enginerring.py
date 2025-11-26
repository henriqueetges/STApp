import streamlit as st
from lib.utils import open_contents
import pandas as pd
import importlib
st.set_page_config(page_title="Data Engineering Porfolio", page_icon="📊")

if "language_selected" not in st.session_state:
    st.session_state.language_selected = 'en-US'

    
language_selection = st.pills(label='Language', options=['en-US', 'pt-BR'], default=st.session_state.language_selected)
st.session_state.language_selected = language_selection

data = open_contents("content/data_engineering.json")
    
content = data['languages'][st.session_state.language_selected]
projects = content['Projects']
st.write(content['Heading'])
st.markdown(content['Description'])
page_selector = st.selectbox("Projects:", [project['Name'] for project in projects])




for project in projects:
    if project['Name'] == page_selector:
        st.title(project['Name'])
        st.write(project['ProjectDescription'])
        tabs = project['Tabs']
        tab_names = [tab['Name'] for tab in tabs]
        selected_tab = st.tabs(tab_names)

        
    
        for i, tab in enumerate(tabs):
            with selected_tab[i]:                
                for content in tab['Contents']:
                    c_type = content["Type"]
                    if c_type == "Header":
                        st.header(content["Description"])
                    elif c_type == "Text":
                        st.write(content["Description"])
                    elif c_type in ["Chart", "Table"]:
                        st.markdown(f"**{content["Name"]}**")
                        st.write(content["Description"])
                        module = importlib.import_module(f"components.{content['module']}")
                        getattr(module, content['function'])(content=content)
        
           
               