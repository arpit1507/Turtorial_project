from src.Tutorial_Project import logger
from src.Tutorial_Project.pipeline.stage_01_data_ingestion import DataIngestionPipeline

try:
    logger.info("Starting data ingestion")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info("Completed data ingestion")
except Exception as e:
    logger.exception(e)
