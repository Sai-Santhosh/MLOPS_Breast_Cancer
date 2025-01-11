import os
import sys
import pandas as pd

from breast_cancer.cloud.s3_syncer import S3Sync
from breast_cancer.exception.exception import BreastCancerException
from breast_cancer.logging.logger import logging
from breast_cancer.constants.training_pipeline import TRAINING_BUCKET_NAME
from breast_cancer.utils.main_utils.utils import load_object
from breast_cancer.utils.main_utils.ml_utils.model.estimator import NetworkModel


class PredictionPipeline:
    def __init__(self):
        self.s3_sync = S3Sync()

    def run_prediction(self, input_file_path: str, output_dir: str = "prediction_output"):
        try:
            # Ensure the output directory exists
            os.makedirs(output_dir, exist_ok=True)

            # Load input data
            logging.info(f"Reading input data from {input_file_path}")
            df = pd.read_csv(input_file_path)

            # Load preprocessor and model
            preprocessor = load_object("final_model/preprocessor.pkl")
            final_model = load_object("final_model/model.pkl")

            if not preprocessor or not final_model:
                raise ValueError("Preprocessor or model not found.")

            # Create network model and make predictions
            network_model = NetworkModel(preprocessor=preprocessor, model=final_model)
            y_pred = network_model.predict(df)

            # Add predictions to the dataframe
            df["predicted_column"] = y_pred

            # Save the output
            output_file_path = os.path.join(output_dir, "output.csv")
            df.to_csv(output_file_path, index=False)
            logging.info(f"Predictions saved at {output_file_path}")

            return output_file_path
        except Exception as e:
            logging.error(f"Prediction failed: {e}")
            raise BreastCancerException(e, sys)

    def sync_prediction_to_s3(self, prediction_file_path: str):
        try:
            aws_bucket_url = f"s3://{TRAINING_BUCKET_NAME}/prediction_output"
            self.s3_sync.sync_file_to_s3(file_path=prediction_file_path, aws_bucket_url=aws_bucket_url)
            logging.info(f"Prediction file {prediction_file_path} synced to S3 bucket at {aws_bucket_url}")
        except Exception as e:
            logging.error(f"Failed to sync prediction output to S3: {e}")
            raise BreastCancerException(e, sys)
