import pyodbc
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

def write_audio_file(phrase, url):
    max_audio_file_key = db_query("SELECT COALESCE(MAX([AudioFile_Key]),0) FROM [tom-ai].[dimAudioFile]").iloc[0,0]
    current_audio_file_key = max_audio_file_key + 1
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db_command(f"INSERT INTO [tom-ai].[dimSession] VALUES ({current_audio_file_key},'{phrase}','{hash(phrase)}','{url}','{timestamp}')")




write_session()