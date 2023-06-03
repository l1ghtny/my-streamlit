import streamlit as st
from components import name_form, faces_form, sidebar, home_page
from authentification import auth
from authentification import login_page


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
