from Tutorial_Project.config.configuration import ConfigurationManager
from Tutorial_Project.components.ModelTraining import Training
from Tutorial_Project import logger

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_training_config = config.get_training_config()
            model_training = Training(config=model_training_config)
            model_training.get_base_model()
            model_training.Training_valid_generator()
            model_training.train([])
        except Exception as e:
            raise e
    
if __name__ == "__main__":
    try:
        logger.info("Starting model training")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info("Completed model training")
    except Exception as e:
        logger.exception(e)
