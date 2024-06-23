import os
import sys

sys.path.append(os.getcwd())
from src.auth.auth import fetch_access_token, verify_access_token


token = fetch_access_token
verify_access_token(token)