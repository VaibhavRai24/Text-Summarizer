import os
import urllib.request as request
from pathlib import Path
import zipfile
from Text_Summarization.logging import logger
from Text_Summarization.utils.common import get_size
from Text_Summarization.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_files(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL, filename= self.config.local_data_file
            )
            logger.info(f"{filename} downloaded successfully with following info : {headers}")
        else:
            logger.info(f"file already exists at {self.config.local_data_file}")
            
            
    def extract_zip_files(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)