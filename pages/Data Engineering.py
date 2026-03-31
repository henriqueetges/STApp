import streamlit as st
from lib.utils import open_contents
from lib.content_renderer import render_group
from pathlib import Path
import json

st.set_page_config(page_title="Portfolio", page_icon="📊", layout="wide")

if "language_selected" not in st.session_state:
    st.session_state["language_selected"] = "en-US"

language_selection = st.pills(label="Language", options=["en-US", "pt-BR"], default=st.session_state.language_selected)
st.session_state.language_selected = language_selection

content_dir = Path(__file__).parent.parent / "content"
json_files = sorted(content_dir.glob("*.json"))

if not json_files:
    st.error("No content JSON files found in the content folder.")
    st.stop()

page_map = {}
for json_file in json_files:
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    lang_data = data.get("languages", {}).get(st.session_state.language_selected)
    if not lang_data:
        lang_data = data.get("languages", {}).get("en-US", {})
    
    heading = lang_data.get("Heading", json_file.stem)
    if heading and heading.startswith("#"):
        heading = heading.lstrip("#").strip()
    
    page_map[heading] = json_file.name

selected_page_title = st.sidebar.selectbox("Select page:", list(page_map.keys()))
json_filename = page_map[selected_page_title]

content = open_contents(f"content/{json_filename}")
lang_data = content.get("languages", {}).get(st.session_state.language_selected, {})

if not lang_data:
    st.error(f"Language data not found for {st.session_state.language_selected}")
    st.stop()

if "Heading" in lang_data:
    st.markdown(lang_data.get("Heading"))
if "Description" in lang_data:
    st.markdown(lang_data.get("Description"))

render_group(lang_data)