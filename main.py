from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import DataModelPreparationPipeline
from cnnClassifier.pipeline.stage_03_training import TrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Base model preparation Stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataModelPreparationPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Training Stage"

try:
   logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
   obj = TrainingPipeline()
   obj.main()
   logger.info(f">>>>>>>> Stage {STAGE_NAME} completed <<<<<<< \n\nx==============x")
except Exception as e:
   logger.exception(e)
   raise e

STAGE_NAME = "Model Evaluation Stage"

try:
   logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
   obj = EvaluationPipeline()
   obj.main()
   logger.info(f">>>>>>>> Stage {STAGE_NAME} completed <<<<<<< \n\nx==============x")
except Exception as e:
   logger.exception(e)
   raise e