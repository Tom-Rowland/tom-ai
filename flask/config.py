import os
from dotenv import load_dotenv

load_dotenv()
try: # This should run locally
    from flask.credentials import OPENAI_TOKEN, RESEMBLEAI_TOKEN, RESEMBLEAI_PROJECTID, RESEMBLEAI_VOICEID

except: # This should run on GitHub Actions
    OPENAI_TOKEN = os.environ['OPENAI_TOKEN']
    RESEMBLEAI_TOKEN = os.environ['RESEMBLEAI_TOKEN']
    RESEMBLEAI_PROJECTID = os.environ['RESEMBLEAI_PROJECTID']
    RESEMBLEAI_VOICEID = os.environ['RESEMBLEAI_VOICEID']