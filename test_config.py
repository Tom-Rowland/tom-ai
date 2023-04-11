def test_secrets():
    from config import OPENAI_TOKEN, RESEMBLEAI_TOKEN, RESEMBLEAI_PROJECTID, RESEMBLEAI_VOICEID
    
    assert 'OPENAI_TOKEN' in locals()
    assert type(OPENAI_TOKEN) == str

    assert 'RESEMBLEAI_TOKEN' in locals()
    assert type(RESEMBLEAI_TOKEN) == str

    assert 'RESEMBLEAI_PROJECTID' in locals()
    assert type(RESEMBLEAI_PROJECTID) == str

    assert 'RESEMBLEAI_VOICEID' in locals()
    assert type(RESEMBLEAI_VOICEID) == str
