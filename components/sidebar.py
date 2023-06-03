import streamlit as st
from auth import logout_button
from util import cookie_manager

def render():
    cookies = cookie_manager.get()
    with st.sidebar:
        st.title('Welcome to my Streamlit App!')
        st.write("User ID: ", cookies.get('user_id'))
        st.write("Username: ", cookies.get('user_username'))

        if st.button('Names'):
            st.session_state['page'] = 'names'

        if st.button('Faces'):
            st.session_state['page'] = 'faces'


        logout_button.render()