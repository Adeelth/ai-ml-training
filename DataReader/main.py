from dataset import Dataset

def main():
    
    url = "https://www.kaggle.com/api/v1/datasets/download/datasnaek/youtube-new"
    folder_path = "data"
    dataset_name = "youtube-new"


    dataset = Dataset(dataset_name, url, folder_path)
    dataset.download()
    dataset.extract()

    dataset.process_dataset()

if __name__ == "__main__":
    main()
