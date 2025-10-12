import streamlit as st
import json

st.set_page_config(page_title="PowerBI Porfolio", page_icon="📊")

if "language_selected" not in st.session_state:
    st.session_state.language_selected = 'en-US'
    
language_selection = st.pills(label='', options=['en-US', 'pt-BR'], default=st.session_state.language_selected)
st.session_state.language_selected = language_selection

with open("content\pbi_portfolio.json","r", encoding='UTF-8') as f:
    data = json.load(f)
    
content = data['languages'][st.session_state.language_selected]
projects = content['Projects']

st.write(f"{content["Heading"]}")
st.sidebar.header("Portfolio")

page_selector = st.sidebar.selectbox("Samples:", [project['Name'] for project in projects] )

for project in projects:
    if project['Name'] == page_selector:
        st.title(project['Name'])
        st.write(project['Description'])




