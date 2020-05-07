import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def Create_Service(client_secret_file,\
    #read-only by default
    scope='https://www.googleapis.com/auth/spreadsheets.readonly',\
    api_service_name='sheets',\
    api_version='v4'):
    
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # But it onlu exists 1 hour, then you have to delete token.pickle to refresh the access
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                client_secret_file, scope)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    try:
        service = build(api_service_name, api_version, credentials=creds)
        print(api_service_name, 'service created successfully')
        return service
    except Exception as e:
        print(e)
        return None