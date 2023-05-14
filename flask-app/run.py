import requests
import time
from flask import Flask
from config import OPENAI_TOKEN, RESEMBLEAI_TOKEN, RESEMBLEAI_PROJECTID, RESEMBLEAI_VOICEID

app = Flask(__name__)


@app.route('/generate_reponse')
def generate_response(chat_history):
    url = 'https://api.openai.com/v1/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + OPENAI_TOKEN}
    data = {
        'model': 'text-davinci-003',
        'prompt': chat_history,
        'max_tokens': 200,
        'temperature': 0.5,
        'top_p': 1,
        'n': 1}
    response = requests.post(url, json=data, headers=headers)
    chat_response = response.json()['choices'][0]['text']
    return chat_response


@app.route('/generate_clip')
def create_clip(body):
    url = f"https://app.resemble.ai/api/v2/projects/{RESEMBLEAI_PROJECTID}/clips"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token token=' + RESEMBLEAI_TOKEN}

    data = {
        'title': body[:256],
        'body': body,
        'voice_uuid': RESEMBLEAI_VOICEID,
        'is_public': False,
        'is_archived': False,
        'callback_uri': 'https://'}

    response = requests.post(url, json=data, headers=headers)
    return response.json()['item']['uuid']


@app.route('/get_clip')
def get_clip(clip_id):
    url = f"https://app.resemble.ai/api/v2/projects/{RESEMBLEAI_PROJECTID}/clips/{clip_id}"
    print(url)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token token=' + RESEMBLEAI_TOKEN}

    while True:
        response = requests.get(url, headers=headers)
        if 'audio_src' in response.json()['item'].keys():
            return response.json()['item']['audio_src']
        time.sleep(1)

print(__name__)
if __name__ == '__main__':
    app.run(debug=True)