import dropbox
from config import get_dbx_instance
from logger import setup_logger
import os

logger = setup_logger()

def check_if_folder_exists(path: str):
    dbx = get_dbx_instance()
    
    try:
        logger.info("Checking if folder exists...")
        dbx.files_get_metadata(path)
        return True
        
    except Exception as e:
        if isinstance(e.error, dropbox.files.GetMetadataError):
            return False
        else:
            logger.error(e)

def retrieve_photo_names(path: str):
    if check_if_folder_exists:
        dbx = get_dbx_instance()
        photo_names = []
    
    try:
        metadata = dbx.files_list_folder(path=path)
        
        for item in metadata.entries:
            if isinstance(item, dropbox.files.FileMetadata):
                photo_names.append(item.name)

    except dropbox.exceptions.ApiError as e:
        print(f"Error listing files in folder {path}: {e}")

    return photo_names

def download_image_as_batch(file_path: str,
                            download_path: str):
    dbx = get_dbx_instance()
    os.makedirs(download_path, exist_ok=True)
    photo_names = retrieve_photo_names(path=file_path)
    # only batch 5 photos as proof of concept
    photo_names = photo_names[:5]
    
    try:                
        for photo in photo_names:
            path = os.path.join(file_path, photo)
            metadata, response = dbx.files_download(path=path)
            
            if response.status_code == 200:
                logger.info(f"Downloading image: {path}")
                
                local_filepath = os.path.join(download_path, photo)
                
                with open(file=local_filepath, mode='wb') as output:
                    output.write(response.content)
            
            else:
                logger.error(f"Response value of {response.status_code}")
    
    except Exception as e:
        if isinstance(e.error, dropbox.files.DownloadError):
            return
        else:
            logger.error(e)              