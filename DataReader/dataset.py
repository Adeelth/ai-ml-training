from pathlib import Path
import requests
from utils import get_logger
from reader import ReaderFactory


logger = get_logger('dataset')

class Dataset:
    def __init__(self, dataset_name, url, folder_path):
        self.dataset_name = dataset_name
        self.url = url
        self.folder_path = folder_path  

        self.out_dir = Path(self.folder_path)
        self.out_dir.mkdir(parents=True, exist_ok=True)
        self.out_path = self.out_dir / f"{self.dataset_name}.zip"

    def download_dataset(self):
        logger.info(f"Downloading dataset {self.dataset_name}")
        try:
            response = requests.get(self.url, stream=True)
            response.raise_for_status()
            with open(self.out_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            logger.info(f"Dataset {self.dataset_name} downloaded successfully to {self.out_path}")
        except Exception as e:
            logger.error(f"Failed to download dataset {self.dataset_name}: {e}")

    def process_dataset(self):
        logger.info(f"Processing dataset {self.dataset_name}")
        try:
            reader = ReaderFactory.get_reader(self.out_path)
            for item in reader.reader():
                logger.info(f"Processed item: {item}")
        except Exception as e:
            logger.error(f"Failed to process dataset {self.dataset_name}: {e}")