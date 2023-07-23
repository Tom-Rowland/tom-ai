import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

def test_secrets():
    from config import OPENAI_TOKEN, RESEMBLEAI_TOKEN, RESEMBLEAI_PROJECTID, RESEMBLEAI_VOICEID, SQLSERVER_USERNAME, SQLSERVER_PASSWORD
    
    assert 'OPENAI_TOKEN' in locals()
    assert type(OPENAI_TOKEN) == str

    assert 'RESEMBLEAI_TOKEN' in locals()
    assert type(RESEMBLEAI_TOKEN) == str

    assert 'RESEMBLEAI_PROJECTID' in locals()
    assert type(RESEMBLEAI_PROJECTID) == str

    assert 'RESEMBLEAI_VOICEID' in locals()
    assert type(RESEMBLEAI_VOICEID) == str

    assert 'SQLSERVER_USERNAME' in locals()
    assert type(SQLSERVER_USERNAME) == str

    assert 'SQLSERVER_PASSWORD' in locals()
    assert type(SQLSERVER_PASSWORD) == str
