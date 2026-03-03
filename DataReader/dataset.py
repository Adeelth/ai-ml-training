class Dataset:
    def __init__(self, link, folder_path):
        self.filepath = link
        self.folder_path = folder_path  

    def dowload_dataset(self):
        return self.data