import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


def render():
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Use local CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style/style.css")

    # ---- LOAD ASSETS ----
    lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
    im_example = Image.open("images/example.png")

    # ---- HEADER SECTION ----
    with st.container():
        st.subheader("Привет, я Антон :wave:")
        st.title("Я тут занимаюсь херней всякой")
        st.write(
            "Решил попробовать набросать на коленке вот такой вот сайтик, потому что почему бы и нет"
        )

    # ---- WHAT I DO ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Зачем это вообще")
            st.write("##")
            st.write(
                """
                Ну чтобы было удобно смотреть всякую информацию по боту.
                Я планирую сделать публичную страничку (например, чтобы было можно смотреть дни рождения более удобным списком),
                а также добавить логин через дискорд, который позволит админам и модерам заходить и смотреть информацию, которая предназначена только для них
                """
            )
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")

    # ---- PROJECTS ----
    with st.container():
        st.write("---")
        st.header("Тут вообще много возможностей, например, можно вот такую красоту делать:")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(im_example)
        with text_column:
            st.write(
                """
                Так что я планирую использовать этот относительно несложный инструмент для создания полноценного сайта.
                Тут будет удобно и статистику по пользователям смотреть, и всякие другие фишки, если мы их прикрутим.
                """
            )
