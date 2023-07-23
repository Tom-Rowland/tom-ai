import pyodbc
import hashlib
import pandas as pd
from datetime import datetime
from config import SQLSERVER_USERNAME, SQLSERVER_PASSWORD

def db_command(command):
    with pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=tcp:tom-rowland-sqlserver.database.windows.net;PORT=1433;DATABASE=sqldatabase;UID='+SQLSERVER_USERNAME+';PWD='+ SQLSERVER_PASSWORD) as conn:
        with conn.cursor() as cursor:
            cursor.execute(command)

def db_query(query):
    with pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=tcp:tom-rowland-sqlserver.database.windows.net;PORT=1433;DATABASE=sqldatabase;UID='+SQLSERVER_USERNAME+';PWD='+ SQLSERVER_PASSWORD) as conn:
        result = pd.read_sql(query, conn)
    return result

def write_session():
    max_session_key = db_query("SELECT COALESCE(MAX([Session_Key]),0) FROM [tom-ai].[dimSession]").iloc[0,0]
    current_session_key = max_session_key + 1
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db_command(f"INSERT INTO [tom-ai].[dimSession] VALUES ({current_session_key},'{timestamp}')")
    return current_session_key

def write_audio_file(phrase, clip_id):
    max_audio_file_key = db_query("SELECT COALESCE(MAX([AudioFile_Key]),0) FROM [tom-ai].[dimAudioFile]").iloc[0,0]
    current_audio_file_key = max_audio_file_key + 1
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    hashed_phrase = hashlib.sha256(phrase.encode('utf-8')).hexdigest()

    db_command(f"""INSERT INTO [tom-ai].[dimAudioFile] VALUES ({current_audio_file_key},'{phrase.replace("'","''")}','{hashed_phrase}','{clip_id}','{timestamp}')""")
    return max_audio_file_key

def write_chat(session_key, audio_file_key,is_user,text):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if is_user:
        db_command(f"""INSERT INTO [tom-ai].[factChat]
                   ([Session_Key], [DateTime_Key], [Text], [IsUser])
                    VALUES ({session_key},'{timestamp}','{text.replace("'","''")}','{int(is_user)}')""")
    else:
        db_command(f"""INSERT INTO [tom-ai].[factChat]
                   ([Session_Key], [AudioFile_Key], [DateTime_Key], [Text], [IsUser])
                    VALUES ({session_key},'{audio_file_key}','{timestamp}','{text.replace("'","''")}','{int(is_user)}')""")
    return 1