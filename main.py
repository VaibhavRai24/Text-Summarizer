from Text_Summarization.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from Text_Summarization.logging import logger
from Text_Summarization.pipeline.stage02_data_valdiation import DataValidationTrainingPipeline
from Text_Summarization.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME = "Data_ingestion_stage"
try:
    logger.info(f"Running stage: {STAGE_NAME}")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f"Stage {STAGE_NAME} completed successfully")
except Exception as e:
    logger.error(f"Stage {STAGE_NAME} failed with error: {str(e)}")
    raise e


STAGE_NAME =  "Data Validation Stage"

try:
    logger.info(f" Running stage : { STAGE_NAME}")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
except Exception as e:
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"Running stage: {STAGE_NAME}")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise e
                