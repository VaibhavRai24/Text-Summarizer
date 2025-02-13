from Text_Summarization.config.configuration import ConfigurationManager
from Text_Summarization.components.model_evaluation import ModelEvaluation
from Text_Summarization.logging import logger

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config= model_evaluation_config)
        model_evaluation_config.evaluate()