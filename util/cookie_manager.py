import os
import streamlit as st
from dotenv import load_dotenv
from util.encrypted_cookie_manager import EncryptedCookieManager
load_dotenv()

client_secret = os.getenv("DISCORD_CLIENT_SECRET")

# This should be on top of your script
cookies = EncryptedCookieManager(
    # This prefix will get added to all your cookie names.
    # This way you can run your app on Streamlit Cloud without cookie name clashes with other apps.
    prefix="streamlit_proxy/",
    # You should really setup a long COOKIES_PASSWORD secret if you're running on Streamlit Cloud.
    password=client_secret,
)

if not cookies.ready():
    # Wait for the component to load and send us current cookies.
    st.stop()


def get():
    return cookies
