import streamlit as st
import json

st.set_page_config(
    page_title="LiveData",
    page_icon="⚽"
)

if "language_selected" not in st.session_state:
    st.session_state.language_selected = 'en-US'
    
language_selection = st.pills(label='', options=['en-US', 'pt-BR'], default='en-US')
st.session_state.language_selected = language_selection

st.title("Live Data")
st.write("The idea is to create an app that takes user input from this website, save its data inSQLite and perform some checks.")
st.image('https://as2.ftcdn.net/v2/jpg/00/08/85/67/1000_F_8856770_vGp3qw2viEt06tqIY55EMwOC84nMBC6x.jpg')