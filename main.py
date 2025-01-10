from breast_cancer.components.data_ingestion import DataIngestion
from breast_cancer.components.data_validation import DataValidation
from breast_cancer.exception.exception import BreastCancerException
from breast_cancer.logging.logger import logging
from breast_cancer.entity.config_entity import DataIngestionConfig, DataValidationConfig
from breast_cancer.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data initiation completed")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info('Initiate data validation')
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info('Data validation done')
    except Exception as e:
        raise BreastCancerException(e,sys)