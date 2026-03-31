import streamlit as st
from lib.utils import open_contents

st.set_page_config(page_title="PowerBI Porfolio", page_icon="📊")

if "language_selected" not in st.session_state:
    st.session_state.language_selected = 'en-US'
    
language_selection = st.pills(label='', options=['en-US', 'pt-BR'], default=st.session_state.language_selected)
st.session_state.language_selected = language_selection

data = open_contents("content/pbi_portfolio.json")
    
content = data['languages'][st.session_state.language_selected]
projects = content['Projects']

st.write(f"{content["Heading"]}")
st.sidebar.header("Portfolio")

page_selector = st.sidebar.selectbox("Projects:", [project['Name'] for project in projects] )

for project in projects:
    if project['Name'] == page_selector:
        st.title(project['Name'])
        st.write(project['Description'])




