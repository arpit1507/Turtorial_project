from src.Tutorial_Project.config.configuration import ConfigurationManager
from src.Tutorial_Project.components.DataIngestion import DataIngestion
from src.Tutorial_Project import logger

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config= ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion= DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    
    
if __name__ == "__main__":
    try:
        logger.info("Starting data ingestion")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info("Completed data ingestion")
    except Exception as e:
        logger.exception(e)




    