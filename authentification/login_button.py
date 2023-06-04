import asyncio
from bokeh.models.widgets import Div

import streamlit as st

from authentification import discord_oauth


def render():
    authorization_url = asyncio.run(
        discord_oauth.write_authorization_url()
    )

    button = st.button('Login')
    if button:
        js = f"window.open({authorization_url})"  # New tab or window
        js = f"window.location.href = '{authorization_url}'"  # Current tab
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

        st.experimental_rerun()
