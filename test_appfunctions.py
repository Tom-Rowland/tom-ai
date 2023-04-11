import app_functions

def test_generate_response():
    from data import tom_context
    chat_history = tom_context + f'\n\n[User]: "testing!"\n\n[Tom]:' 
    response = app_functions.generate_response(chat_history)
    print(response)
    assert(type(response)==str)

def test_create_clip():
    text = "Hi, this is a test"
    clip_id = app_functions.create_clip(text)
    print(clip_id)
    assert len(clip_id) == 8 and type(clip_id) == str

def test_get_clip():
    clip_id = app_functions.create_clip('this is a test clip')
    clip_url = app_functions.get_clip(clip_id)
    print(clip_url)

    assert type(clip_url == str) and clip_url[-4:] == '.wav'