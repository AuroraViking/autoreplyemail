### gmail_service.py
```python
import base64
import os
from email.message import EmailMessage
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def get_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def get_unread_messages():
    service = get_service()
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:unread").execute()
    messages = results.get('messages', [])
    detailed_messages = []
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        detailed_messages.append(msg_data)
    return detailed_messages

def create_draft(original_msg, reply_text):
    service = get_service()
    headers = original_msg['payload']['headers']
    subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "(no subject)")
    to = next((h['value'] for h in headers if h['name'] == 'From'), None)

    message = EmailMessage()
    message.set_content(reply_text)
    message['To'] = to
    message['From'] = 'me'
    message['Subject'] = f"Re: {subject}"

    encoded = base64.urlsafe_b64encode(message.as_bytes()).decode()
    create_message = {'message': {'raw': encoded}}

    service.users().drafts().create(userId='me', body=create_message).execute()
```
