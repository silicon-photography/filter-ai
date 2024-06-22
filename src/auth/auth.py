import dropbox
import os
import sys
import requests
from src.logger import setup_logger
sys.path.append(os.getcwd())

logger = setup_logger()


def fetch_access_token() -> str:
    """
    Fetches a token for access to the Dropbox API

    Returns:
        str: access token
    """
    response = requests.post(url="https://api.dropbox.com/oauth2/token",
                             data={
                                 "grant_type": "refresh_token",
                                 "refresh_token": os.environ['REFRESH_TOKEN'],
                                 "client_id": os.environ['APP_KEY'],
                                 "client_secret": os.environ['APP_SECRET'] 
                             })
    
    if 'access_token' in response.json():
        return response.json()['access_token']
    else:
        raise Exception(f"Error obtaining access token: {response.json()}")

def verify_access_token(access_token: str) -> None:
    """
    Checks to see if an access token is valid, if it is not it will create a new one

    Args:
        access_token (str): Dropbox API token
    """
    try:
        dbx = dropbox.Dropbox(oauth2_access_token=access_token)
        logger.info(f"Verifying access token...")
        account_info = dbx.users_get_current_account()
        logger.info(f"Access obtained...")
        
    except Exception as e:
        logger.error(f"Access token expired or invalid: {e}")
        logger.info(f"Refreshing a new access token...")
        access_token = fetch_access_token()
        verify_access_token(access_token=access_token)