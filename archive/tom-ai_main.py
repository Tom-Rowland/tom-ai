import streamlit as st
import flask.app_functions as app_functions
from flask.data import tom_context
from flask.config import OPENAI_TOKEN, RESEMBLEAI_TOKEN, RESEMBLEAI_PROJECTID,RESEMBLEAI_VOICEID
import os

st.title("tom.ai")
st.text("Start by saying hello")

if 'count' not in st.session_state:
    st.session_state.count = 0

i = 0

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = tom_context

while True:
    text = st.text_input(" ", key=f"text_input_{i}")
    
    if not text:
        break
    
    if i == st.session_state.count:
        st.session_state.chat_history += f'\n\n[User]: {text}\n\n[Tom]: '
        del text
        # Generate response to input with ChatGPT
        response = app_functions.generate_response(st.session_state.chat_history)
        st.session_state.chat_history += str(response)
        
        # Create clip in resemble.ai of the response and return the new clip's uid
        clip_id = app_functions.create_clip(response)
        
        # Get audio file url from resemble.ai
        audio_file = app_functions.get_clip(clip_id)
        
        # Render audio in web
        st.audio(audio_file, format='audio/wav')
        st.session_state.count += 1
    i += 1