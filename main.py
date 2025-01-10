from breast_cancer.components.data_ingestion import DataIngestion
from breast_cancer.exception.exception import BreastCancerException
from breast_cancer.logging.logger import logging
from breast_cancer.entity.config_entity import DataIngestionConfig
from breast_cancer.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    except Exception as e:
        raise BreastCancerException(e,sys)