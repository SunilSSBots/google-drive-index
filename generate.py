import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

credentials = None
__G_DRIVE_TOKEN_FILE = "token.pickle"
#Add Manually Any Api Auth
__OAUTH_SCOPE = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/youtube.force-ssl"
]

json_files = [f for f in os.listdir() if f.endswith(".json")]
if not json_files:
    raise FileNotFoundError("No .json credential file found.")
client_secret_file = json_files[0] 

if os.path.exists(__G_DRIVE_TOKEN_FILE):
    with open(__G_DRIVE_TOKEN_FILE, 'rb') as f:
        credentials = pickle.load(f)
        if (
            credentials and
            credentials.expired and
            credentials.refresh_token
        ):
            credentials.refresh(Request())
else:
    flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, __OAUTH_SCOPE)
    credentials = flow.run_local_server(port=0, open_browser=False)

with open(__G_DRIVE_TOKEN_FILE, 'wb') as token:
    pickle.dump(credentials, token)
