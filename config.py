import os
from dotenv import load_dotenv

load_dotenv()
try: # This should run locally
    from credentials import OPENAI_TOKEN, RESEMBLEAI_TOKEN, RESEMBLEAI_PROJECTID, RESEMBLEAI_VOICEID, SQLSERVER_USERNAME, SQLSERVER_PASSWORD

except: # This should run on GitHub Actions
    OPENAI_TOKEN = os.environ['OPENAI_TOKEN']
    RESEMBLEAI_TOKEN = os.environ['RESEMBLEAI_TOKEN']
    RESEMBLEAI_PROJECTID = os.environ['RESEMBLEAI_PROJECTID']
    RESEMBLEAI_VOICEID = os.environ['RESEMBLEAI_VOICEID']
    SQLSERVER_USERNAME = os.environ['SQLSERVER_USERNAME']
    SQLSERVER_PASSWORD = os.environ['SQLSERVER_PASSWORD']