import dropbox
import os
from logger import setup_logger

_dbx_instance = None

def get_dbx_instance():
    global _dbx_instance
    if _dbx_instance is None:
        _dbx_instance = dropbox.Dropbox(
            app_key=os.environ['APP_KEY'],
            app_secret=os.environ['APP_SECRET'],
            oauth2_refresh_token=os.environ["REFRESH_TOKEN"]
        )
    return _dbx_instance