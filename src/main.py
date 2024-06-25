import os
import sys

sys.path.append(os.getcwd())
from src.auth.auth import fetch_access_token, verify_access_token
from src.ingestion import download_image_as_batch

# should run each time someone accesses the page
token = fetch_access_token
verify_access_token(token)

# test download
download_image_as_batch("/PHOTOS-EXPORTED/2024-06-15-Shaurya-Upanayanam-Ceremony-Sandya-Samarth-Sthirah-Family-V1-S12-MF-WN-105-FINAL/",
               "test")