import streamlit as st 

def render():
    hair_color = st.color_picker("Hair Color")
    eye_color = st.selectbox("Eye Color", ["Brown", "Blue", "Green", "Hazel"])

    is_complete = hair_color and eye_color
    submit_button = st.button("Submit", disabled= not is_complete)

    if submit_button:
        st.write(f"My face includes {hair_color} hair and {eye_color} eyes.")