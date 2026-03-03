from pathlib import Path
import requests
from utils import get_logger
from reader import ReaderFactory
import glob
import os
import concurrent.futures
import zipfile



logger = get_logger('dataset')

class Dataset:
    def __init__(self, dataset_name, url, folder_path):
        self.dataset_name = dataset_name
        self.url = url
        self.folder_path = folder_path  

        self.out_dir = Path(self.folder_path)
        self.out_dir.mkdir(parents=True, exist_ok=True)
        self.out_path = self.out_dir / f"{self.dataset_name}.zip"

    def extract(self):
        
        extract_path = self.out_dir / f"{self.dataset_name}"

        with zipfile.ZipFile(self.out_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
            print(f"Files extracted to {extract_path}")

    def download(self):
        logger.info(f"Downloading dataset {self.dataset_name}")
        try:
            response = requests.get(self.url, stream=True, timeout=30)
            response.raise_for_status()
            with open(self.out_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            logger.info(f"Dataset {self.dataset_name} downloaded successfully to {self.out_path}")

        except Exception as e:
             logger.error(f"Failed to download dataset {self.dataset_name}: {e}")
           

  


    def process_file(self, filepath):
        logger.info(f"Processing file {filepath}")
        try:
            reader = ReaderFactory.get_reader(filepath)
            for item in reader.reader():
                logger.info(f"Processed item in file {filepath}: {item}")
        except Exception as e:
            logger.error(f"Failed to process file {filepath}: {e}")

    def process_dataset(self):
        logger.info(f"Processing dataset {self.dataset_name}")
      
        all_files = glob.glob(os.path.join(self.folder_path, "**", "*.*"), recursive=True)
        target_files = [f for f in all_files if f.endswith(('.csv', '.json', '.txt'))]
        logger.info(f"Found {len(target_files)} target files for processing.")

        all_processed_data = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_file = {executor.submit(self.process_file, filepath): filepath for filepath in target_files}
            for future in concurrent.futures.as_completed(future_to_file):
                filepath = future_to_file[future]
                try:
                    data = future.result()
                    if data:
                        all_processed_data.extend(data)
                except Exception as exc:
                    logger.error(f"{filepath} generated an exception: {exc}")