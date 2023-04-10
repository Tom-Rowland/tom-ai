import os
from dotenv import load_dotenv

load_dotenv()
try: # This should run locally
    from credentials import credentials_dict
    OPENAI_TOKEN = credentials_dict['openai_token']
    RESEMBLEAI_TOKEN = credentials_dict['resembleai']['token']
    RESEMBLEAI_PROJECTID = credentials_dict['resembleai']['projectid']
    RESEMBLEAI_VOICEID = credentials_dict['resembleai']['voiceid']
except: # This should run on GitHub Actions
    OPENAI_TOKEN = os.environ['OPENAI_TOKEN']
    RESEMBLEAI_TOKEN = os.environ['RESEMBLEAI_TOKEN']
    RESEMBLEAI_PROJECTID = os.environ['RESEMBLEAI_PROJECTID']
    RESEMBLEAI_VOICEID = os.environ['RESEMBLEAI_VOICEID']