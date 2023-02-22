from __future__ import print_function

import os.path
import os
import csv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID of a sample document.
DOCUMENT_ID = os.environ['CM_GOOGLE_SPREADSHEET_ID']


def main():
    """Shows basic usage of the Docs API.
    Prints the title of a sample document.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)
        sheet_name = os.environ.get('CM_GOOGLE_SHEET_NAME', 'Sheet1')
        csv_file = os.environ['CM_CSV_FILE_PATH']

        f = open(csv_file, "r")
        values = [r for r in csv.reader(f)]
        request = service.spreadsheets().values().update(spreadsheetId=DOCUMENT_ID, range=sheet_name, valueInputOption="USER_ENTERED", body={"values": values}).execute()

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()
