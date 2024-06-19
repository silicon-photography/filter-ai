import dropbox
import os
import sys

sys.path.append(os.getcwd())



dbx = dropbox.Dropbox(os.environ['DROPBOX_API_KEY'])

def check_token(dbx):
    try:
        account_info = dbx.users_get_current_account()
        print(f"Account name: {account_info.name.display_name}")
        print(f"Email: {account_info.email}")
    except dropbox.exceptions.AuthError as err:
        print(f"Authentication error: {err}")

check_token(dbx)

