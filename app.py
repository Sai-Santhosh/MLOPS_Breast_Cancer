import sys
import os

import certifi
ca = certifi.where()

from dotenv import load_dotenv
load_dotenv()
mongo_db_url = os.getenv("MONGO_DB_URL")
print(mongo_db_url)

import pymongo
from breast_cancer.exception.exception import BreastCancerException
from breast_cancer.logging.logger import logging
from breast_cancer.pipeline.training_pipeline import TrainingPipeline
from breast_cancer.pipeline.prediction_pipeline import PredictionPipeline
from breast_cancer.constants.training_pipeline import TRAINING_BUCKET_NAME
from breast_cancer.cloud.s3_syncer import S3Sync
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd

from breast_cancer.utils.main_utils.utils import load_object
from breast_cancer.utils.main_utils.ml_utils.model.estimator import NetworkModel

client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

from breast_cancer.constants.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from breast_cancer.constants.training_pipeline import DATA_INGESTION_DATABASE_NAME

database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="./templates")

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response("Training is successful")
    except Exception as e:
        raise BreastCancerException(e, sys)

@app.post("/predict")
async def predict_route(request: Request, file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)

        preprocessor = load_object("final_model/preprocessor.pkl")
        final_model = load_object("final_model/model.pkl")

        if not preprocessor or not final_model:
            return Response("Preprocessor or model is not found.", status_code=500)

        network_model = NetworkModel(preprocessor=preprocessor, model=final_model)
        y_pred = network_model.predict(df)

        df['predicted_column'] = y_pred

        output_dir = "prediction_output"
        os.makedirs(output_dir, exist_ok=True)

        output_file_path = os.path.join(output_dir, "output.csv")
        df.to_csv(output_file_path, index=False)

        s3_sync = S3Sync()
        aws_bucket_url = f"s3://{TRAINING_BUCKET_NAME}/prediction_output/output.csv"
        s3_sync.sync_file_to_s3(file_path=output_file_path, aws_bucket_url=aws_bucket_url)

        table_html = df.to_html(classes='table table-striped')
        return templates.TemplateResponse("table.html", {"request": request, "table": table_html})

    except Exception as e:
        logging.error(f"Prediction failed: {e}")
        raise BreastCancerException(e, sys)


if __name__ == "__main__":
    app_run(app, host="0.0.0.0", port=8000)