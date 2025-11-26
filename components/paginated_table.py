import streamlit as st
import pandas as pd

def load_df(df_path):
    data = pd.read_csv(df_path, sep=',')
    return data

def render(content):
    # Calculate total pages
    df = load_df(content['path'])
    page_size = content['pages']
    
    total_rows = len(df)
    total_pages = (total_rows - 1) // page_size + 1
    page_key = f"{content['Name']}_page_number"

    # Keep track of current page in session state
    if page_key not in st.session_state:
        st.session_state[page_key] = 0

    # Slice dataframe for current page
    start =  st.session_state[page_key] * page_size
    end = start + page_size
    st.dataframe(df.iloc[start:end])
    # Navigation buttons
    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        if st.button("⬅️ Prev", key=f"{content['Name']}_prev") and  st.session_state[page_key] > 0:
            st.session_state[page_key] -= 1
    with col3:
        if st.button("Next ➡️", key=f"{content['Name']}_next") and  st.session_state[page_key]  < total_pages - 1:
            st.session_state[page_key]  += 1
    st.write(f"Page { st.session_state[page_key] +1} of {total_pages}")
