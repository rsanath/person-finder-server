from google.cloud import storage

config_file_path = 'cloud_storage/gcs_storage_key.json'

# buckets
IMG_PROCESS_OUTPUT_BUCKET = 'image-processing-outputs'
SEARCHEE_SAMPLE_BUCKET = 'searchee-samples'
FIR_BUCKET = 'fir-bucket'

client = storage.Client.from_service_account_json(config_file_path)