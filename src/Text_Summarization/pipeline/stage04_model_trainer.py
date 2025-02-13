from Text_Summarization.config.configuration import ConfigurationManager
from Text_Summarization.components.model_trainer import ModelTrainer
from Text_Summarization.logging import logger

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    
    logger.info("Initiated the model training pipeline")
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.model_trainer_config()
        model_trainer_config = ModelTrainer(config= model_trainer_config)
        model_trainer_config.train()