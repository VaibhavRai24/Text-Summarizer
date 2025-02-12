from Text_Summarization.config.configuration import ConfigurationManager
from Text_Summarization.components.data_validation import DataValidation
from Text_Summarization.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_files_exist()