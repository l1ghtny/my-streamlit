import streamlit as st
from components import name_form, faces_form, sidebar, home_page

sidebar.render()

if "page" not in st.session_state:
    home_page.render()

else:
    page = st.session_state['page']
    if page == "names":
        name_form.render()
    else:
        faces_form.render()
