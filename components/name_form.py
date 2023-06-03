import streamlit as st 

def render():
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")

    is_complete = first_name and last_name
    submit_button = st.button("Submit", disabled= not is_complete)

    if submit_button:
        st.write(f"My name is {first_name} {last_name} and this is my first streamlit app")