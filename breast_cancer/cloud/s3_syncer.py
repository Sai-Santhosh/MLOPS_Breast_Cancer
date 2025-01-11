import os
from breast_cancer.logging.logger import logging

class S3Sync:
    def sync_folder_to_s3(self, folder, aws_bucket_url):
        try:
            command = f"aws s3 sync {folder} {aws_bucket_url} "
            logging.info(f"Syncing folder: {folder} to bucket: {aws_bucket_url}")
            os.system(command)
        except Exception as e:
            logging.error(f"Error syncing folder {folder} to S3: {e}")
            raise

    def sync_folder_from_s3(self, folder, aws_bucket_url):
        try:
            command = f"aws s3 sync {aws_bucket_url} {folder} "
            logging.info(f"Syncing bucket: {aws_bucket_url} to folder: {folder}")
            os.system(command)
        except Exception as e:
            logging.error(f"Error syncing S3 bucket {aws_bucket_url} to folder {folder}: {e}")
            raise

    def sync_file_to_s3(self, file_path, aws_bucket_url):
        try:
            command = f"aws s3 cp {file_path} {aws_bucket_url}"
            logging.info(f"Syncing file: {file_path} to bucket: {aws_bucket_url}")
            os.system(command)
        except Exception as e:
            logging.error(f"Error syncing file {file_path} to S3: {e}")
            raise
