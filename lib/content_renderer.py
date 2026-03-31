import streamlit as st
import importlib


def render_content_item(content: dict):
    c_type = content.get("Type", "")

    if c_type == "Header":
        st.header(content.get("Description", ""))
        return

    if c_type == "Text":
        st.write(content.get("Description", ""))
        return

    if c_type in ("Chart", "Table"):
        st.markdown(f"**{content.get('Name', '')}**")
        st.write(content.get("Description", ""))

        module_name = content.get("module")
        function_name = content.get("function")
        if not module_name or not function_name:
            st.warning("Missing module/function configuration for Chart/Table content.")
            return

        try:
            module = importlib.import_module(f"components.{module_name}")
            render_fn = getattr(module, function_name)
            render_fn(content=content)
        except Exception as err:
            st.error(f"Error rendering {c_type} '{content.get('Name', '')}': {err}")
        return

    st.warning(f"Unhandled content type: {c_type}")


def render_project(project: dict):
    title = project.get("Name", "Unnamed project")
    st.subheader(title)

    description = project.get("ProjectDescription") or project.get("Description")
    if description:
        st.write(description)

    tabs = project.get("Tabs")
    if tabs:
        tab_labels = [tab.get("Name", "Untitled") for tab in tabs]
        tab_objects = st.tabs(tab_labels)

        for i, tab in enumerate(tabs):
            with tab_objects[i]:
                for content in tab.get("Contents", []):
                    render_content_item(content)

        return

    # fallback: if no tabs, render minimal project body
    for content in project.get("Contents", []):
        render_content_item(content)


def render_group(group: dict):
    projects = group.get("Projects", [])
    if not projects:
        st.info("No projects found.")
        return

    for idx, project in enumerate(projects, start=1):
        render_project(project)
        if idx < len(projects):
            st.divider()