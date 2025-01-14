from Text_Summarization.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from Text_Summarization.logging import logger


STAGE_NAME = "Data_ingestion_stage"
try:
    logger.info(f"Running stage: {STAGE_NAME}")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f"Stage {STAGE_NAME} completed successfully")
except Exception as e:
    logger.error(f"Stage {STAGE_NAME} failed with error: {str(e)}")
    raise e