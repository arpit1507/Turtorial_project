from src.Tutorial_Project import logger
from src.Tutorial_Project.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.Tutorial_Project.pipeline.stage_02_Prepared_Base_Model import BaseModelPreparationPipeline
from src.Tutorial_Project.pipeline.stage_03_Training import ModelTrainingPipeline
from src.Tutorial_Project.pipeline.stage_04_Mlflow_integeration import EvaluationPipeline

"""
try:
    logger.info("Starting data ingestion")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info("Completed data ingestion")
except Exception as e:
    logger.exception(e)
"""

"""try:
    logger.info("Starting base model preparation")
    obj = BaseModelPreparationPipeline()
    obj.main()
    logger.info("Completed base model preparation")
except Exception as e:
    logger.exception(e)"""

"""
try:
    logger.info("Starting model training")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info("Completed model training")
except Exception as e:
    logger.exception(e)
"""

try:
    logger.info("Starting model evaluation")
    obj = EvaluationPipeline()
    obj.main()
    logger.info("Completed model evaluation")
except Exception as e:
    logger.exception(e)
    