import asyncio
import webbrowser

import streamlit as st

from authentification import discord_oauth


def render():
    authorization_url = asyncio.run(
        discord_oauth.write_authorization_url()
    )

    button = st.button('Login')
    if button:
        webbrowser.open(authorization_url)
