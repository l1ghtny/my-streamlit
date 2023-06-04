import streamlit as st
from authentification import logout_button, login_button, auth
from util import cookie_manager


def render():
    cookies = cookie_manager.get()
    with st.sidebar:
        if not auth.is_logged_in():
            st.title(f'Привет, {cookies.get("username")}')
            st.write("User ID: ", cookies.get('user_id'))
            st.write("Username: ", cookies.get('user_username'))
        else:
            st.title('Привет!')
            st.write("User ID: ", cookies.get('user_id'))
            st.write("Username: ", cookies.get('user_username'))

        # if st.button('Names'):
        #     st.session_state['page'] = 'names'
        #
        # if st.button('Faces'):
        #     st.session_state['page'] = 'faces'

        if not auth.is_logged_in():
            login_button.render()
        else:
            logout_button.render()
