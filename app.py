import streamlit as st
from components import name_form, faces_form, sidebar, home_page
from auth import auth
from auth import login_page

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

if not auth.is_logged_in():
    login_page.render()

else:
    sidebar.render()

    if not "page" in st.session_state:
        home_page.render()

    else:
        page = st.session_state['page']
        if page == "names":
            name_form.render()
        else:
            faces_form.render()
