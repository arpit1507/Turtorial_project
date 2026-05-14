from src.Tutorial_Project import logger
from src.Tutorial_Project.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.Tutorial_Project.pipeline.stage_02_Prepared_Base_Model import BaseModelPreparationPipeline

"""
try:
    logger.info("Starting data ingestion")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info("Completed data ingestion")
except Exception as e:
    logger.exception(e)
"""

try:
    logger.info("Starting base model preparation")
    obj = BaseModelPreparationPipeline()
    obj.main()
    logger.info("Completed base model preparation")
except Exception as e:
    logger.exception(e)
