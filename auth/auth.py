import streamlit as st, json, os, asyncio

from auth import discord_oauth
from util import cookie_manager

def is_logged_in():
    cookies = cookie_manager.get()

    if not 'token' in cookies or cookies['token'] == '':
        try:
            code = st.experimental_get_query_params()['code']
        except:
            return False

        else:
            # Verify token is correct:
            try:
                token = asyncio.run(
                    discord_oauth.write_access_token(code)
                )

            except:
                return False

            else:
                if token.is_expired():
                    return False

                else:
                    cookies['token'] = json.dumps(token)

                    user_id, user_data = asyncio.run(
                        discord_oauth.get_id_data(token['access_token'])
                    )

                    cookies['user_id'] = user_id
                    cookies['user_username'] = user_data['username'] + '#' + user_data['discriminator']

                    cookies.save()
                    st.experimental_set_query_params()

                    return True

    else:
        token = discord_oauth.json_str_to_token(cookies['token'])

        return not token.is_expired()
