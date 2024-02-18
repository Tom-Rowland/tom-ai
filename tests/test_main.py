import app_functions
from data import tom_context

def test_3_consecutive_inputs():
    chat_history = [
        {
            "role": "system",
            "content": tom_context
        }
    ]

    input_1 = 'Hello, is this a test?'
    chat_history.append({
        "role": "user",
        "content": input_1
    })

    response1 = app_functions.generate_response(chat_history)
    chat_history.append({
        "role": "assistant",
        "content": str(response1)
    })
    clip_id1, body = app_functions.create_clip(response1)
    audio_file1, key = app_functions.get_clip(clip_id1, body)
    print(chat_history)

    input_2 = 'Are you sure about that?'
    chat_history.append({
        "role": "user",
        "content": input_2    
    })
    response2 = app_functions.generate_response(chat_history)
    chat_history.append({
        "role": "assistant",
        "content": str(response2)
    })
    clip_id2, body2 = app_functions.create_clip(response2)
    audio_file2, key2 = app_functions.get_clip(clip_id2, body2)
    print(chat_history)

    input_3 = 'Well as long as you are sure then I am happy.'
    chat_history.append({
        "role": "user",
        "content": input_3    
    })
    response3 = app_functions.generate_response(chat_history)
    chat_history.append({
        "role": "assistant",
        "content": str(response3)
    })
    clip_id2, body2 = app_functions.create_clip(response2)
    audio_file2, key2 = app_functions.get_clip(clip_id2, body2)
    print(chat_history)
    clip_id3, body3 = app_functions.create_clip(response3)
    audio_file3, key3 = app_functions.get_clip(clip_id3, body3)
    print(chat_history)

    assert chat_history[0] == {
            "role": "system",
            "content": tom_context
        }
    
    assert chat_history[1] == {
            "role": "user",
            "content": input_1
        }
    
    assert chat_history[2] == {
            "role": "assistant",
            "content": response1
        }
    
    assert chat_history[3] == {
            "role": "user",
            "content": input_2
        }
    
    assert chat_history[4] == {
            "role": "assistant",
            "content": response2
        }

    assert chat_history[5] == {
            "role": "user",
            "content": input_3
        }
    
    assert chat_history[6] == {
            "role": "assistant",
            "content": response3
        }