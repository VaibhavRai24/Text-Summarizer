import os
from Text_Summarization.logging import logger
from Text_Summarization.entity.DataIngestionConfig import DataValidationConfig


"""
Going to make a class for data Validation 

"""
class DataValidation:
    def __init__(self, config:DataValidationConfig):
        self.config = config
        
        
    def validate_all_files_exist(self) ->bool:
        logger.info("Starting the validation of files")
        try:
            validation_status = None
            
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))
            for files in all_files:
                if files not in all_files:
                    validation_status = False
                    with open(self.config.STATUS_FILE,  'w') as f:
                        f.write(f"Validation status is : {validation_status} ")
                        
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE,  'w') as f:
                        f.write(f"Validation status is : {validation_status} ")
                        
            return validation_status
        
        except Exception as e:
            raise e