from Tutorial_Project.config.configuration import ConfigurationManager
from Tutorial_Project.components.PreparedBaseModel import PreparedBaseModel
from Tutorial_Project import logger

class BaseModelPreparationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            prepared_base_model_config = config.get_prepared_base_model_config()
            prepared_base_model = PreparedBaseModel(config=prepared_base_model_config)
            prepared_base_model.get_base_model()
            prepared_base_model.update_base_model()
        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try:
        logger.info("Starting base model preparation")
        obj = BaseModelPreparationPipeline()
        obj.main()
        logger.info("Completed base model preparation")
    except Exception as e:
        logger.exception(e)

        

