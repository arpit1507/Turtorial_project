from src.Tutorial_Project.config.configuration import ConfigurationManager
from src.Tutorial_Project.components.Mlflow import Evaluation
from src.Tutorial_Project import logger

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            evaluation = Evaluation(eval_config)
            evaluation.evaluation()
            evaluation.save_score()
            # evaluation.log_into_mlflow()
        except Exception as e:
            raise e
        
if __name__ == "__main__":
    try:
        logger.info("Starting model evaluation")
        obj = EvaluationPipeline()
        obj.main()
        logger.info("Completed model evaluation")
    except Exception as e:
        logger.exception(e)
        