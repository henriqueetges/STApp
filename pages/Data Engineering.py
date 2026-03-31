import streamlit as st
from lib.utils import open_contents
from lib.data_engineering_renderer import render_group
from pathlib import Path
import json

st.set_page_config(page_title="Portfolio", page_icon="📊", layout="wide")

if "language_selected" not in st.session_state:
    st.session_state["language_selected"] = "en-US"

language_selection = st.pills(label="Language", options=["en-US", "pt-BR"], default=st.session_state.language_selected)
st.session_state.language_selected = language_selection

# Discover all JSON content files dynamically
content_dir = Path(__file__).parent.parent / "content"
json_files = sorted(content_dir.glob("*.json"))

if not json_files:
    st.error("No content JSON files found in the content folder.")
    st.stop()

# Extract page titles from JSON headings
page_map = {}
for json_file in json_files:
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Get heading from current language, fallback to en-US
    lang_data = data.get("languages", {}).get(st.session_state.language_selected)
    if not lang_data:
        lang_data = data.get("languages", {}).get("en-US", {})
    
    heading = lang_data.get("Heading", json_file.stem)
    if heading and heading.startswith("#"):
        heading = heading.lstrip("#").strip()
    
    page_map[heading] = json_file.name

# Sidebar: page selector
selected_page_title = st.sidebar.selectbox("Select page:", list(page_map.keys()))
json_filename = page_map[selected_page_title]

# Load and render the selected content
content = open_contents(f"content/{json_filename}")
lang_data = content.get("languages", {}).get(st.session_state.language_selected, {})

if not lang_data:
    st.error(f"Language data not found for {st.session_state.language_selected}")
    st.stop()

# Display heading and description
if "Heading" in lang_data:
    st.markdown(lang_data.get("Heading"))
if "Description" in lang_data:
    st.markdown(lang_data.get("Description"))

# Render all projects in the group
render_group(lang_data)