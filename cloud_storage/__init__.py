from google.cloud import storage

config_file_path = 'cloud_storage/Kodona-eb1224097261.json'


# buckets
IMG_PROCESS_OUTPUT_BUCKET = 'image-processing-outputs'


storage_client = storage.Client.from_service_account_json(config_file_path)