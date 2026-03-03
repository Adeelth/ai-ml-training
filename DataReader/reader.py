from utils import get_logger
import csv
import json
import os

logger = get_logger('reader')

class BaseReader:
    def __init__(self,filepath):
        self.filepath = filepath

class CSVReader(BaseReader):
    def  __init__(self, filepath):
        super().__init__(filepath)

    def reader(self):
        logger.info(f"Reading CSV file: {self.filepath}")
        data = []
        try:
            with open(self.filepath, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for idx, row in enumerate(reader):
                   yield row
        except Exception as e:
            logger.error(f"Error reading CSV {self.filepath}: {e}")
     

class JSONReader(BaseReader):
    def  __init__(self, filepath):
        super().__init__(filepath)

    def reader(self):
        logger.info(f"Reading JSON file: {self.filepath}")
        try:
            with open(self.filepath, mode='r', encoding='utf-8') as f:
                content = json.load(f)
                if isinstance(content, list):
                    for item in content:
                        yield item
        except Exception as e:
            logger.error(f"Error reading JSON {self.filepath}: {e}")


class TXTReader(BaseReader):
    def  __init__(self, filepath):
        super().__init__(filepath)
        
    def reader(self):
        logger.info(f"Reading TXT file: {self.filepath}")
        try:
            with open(self.filepath, mode='r', encoding='utf-8') as f:
                for line in f:
                    yield line.strip()
        except Exception as e:
            logger.error(f"Error reading TXT {self.filepath}: {e}") 

class ReaderFactory:
    @staticmethod
    def get_reader(filepath):
        _, ext = os.path.splitext(filepath)
        ext = ext.lower()
        if ext == '.csv':
            return CSVReader(filepath)
        elif ext == '.json':
            return JSONReader(filepath)
        elif ext == '.txt':
            return TXTReader(filepath)
        else:
            raise ValueError(f"Unsupported file extension: {ext}")