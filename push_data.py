import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo
from breast_cancer.exception.exception import BreastCancerException
from breast_cancer.logging.logger import logging

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")

ca=certifi.where()

class BreastCancerDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise BreastCancerException(e,sys)
    
    def csv_to_json(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise BreastCancerException(e,sys)
    
    def insert_into_mongo(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            return BreastCancerException(e,sys)
        
if __name__=='__main__':
    FILE_PATH='raw_data\data.csv'
    DATABASE='santu'
    Collection='Breast_Cancer'
    breastcancerobj=BreastCancerDataExtract()
    records=breastcancerobj.csv_to_json(file_path=FILE_PATH)
    print(records)
    no_of_records=breastcancerobj.insert_into_mongo(records,DATABASE,Collection)
    print(no_of_records)
