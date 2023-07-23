import app_functions
from data import tom_context

def test_3_consecutive_inputs():
    chat_history = tom_context

    input_1 = 'Hello, is this a test?'
    chat_history += f'\n\n[User]: {input_1}\n\n[Tom]: '
    response1 = app_functions.generate_response(chat_history)
    chat_history += str(response1)
    clip_id1, body = app_functions.create_clip(response1)
    audio_file1, key = app_functions.get_clip(clip_id1, body)
    print(chat_history)

    input_2 = 'Are you sure about that?'
    chat_history += f'\n\n[User]: {input_2}\n\n[Tom]: '
    response2 = app_functions.generate_response(chat_history)
    chat_history += str(response2)
    clip_id2, body2 = app_functions.create_clip(response2)
    audio_file2, key2 = app_functions.get_clip(clip_id2, body2)
    print(chat_history)

    input_3 = 'Well as long as you are sure then I am happy.'
    chat_history += f'\n\n[User]: {input_3}\n\n[Tom]: '
    response3 = app_functions.generate_response(chat_history)
    chat_history += str(response3)
    clip_id3, body3 = app_functions.create_clip(response3)
    audio_file3, key3 = app_functions.get_clip(clip_id3, body3)
    print(chat_history)

    assert chat_history == tom_context + f'\n\n[User]: {input_1}\n\n[Tom]: ' + response1\
                                       + f'\n\n[User]: {input_2}\n\n[Tom]: ' + response2\
                                       + f'\n\n[User]: {input_3}\n\n[Tom]: ' + response3
