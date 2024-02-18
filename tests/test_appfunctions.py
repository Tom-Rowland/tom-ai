import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import app_functions

def test_generate_response():
    from data import tom_context
    chat_history = [
        {
            "role": "system",
            "content": tom_context
        },
        {
            "role": "user",
            "content": "testing!"
        }
    ]
    response = app_functions.generate_response(chat_history)
    print(response)
    assert(type(response)==str)

def test_create_clip():
    text = "Hi, this is a test"
    clip_id, body = app_functions.create_clip(text)
    print(clip_id)
    assert len(clip_id) == 8 and type(clip_id) == str

def test_get_clip():
    clip_id, body = app_functions.create_clip('this is a test clip')
    clip_url, key = app_functions.get_clip(clip_id, body)
    clip_url, key

    assert type(clip_url == str) and clip_url[-4:] == '.wav'
    assert type(key == int)