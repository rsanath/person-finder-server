from . import client
from . import IMG_PROCESS_OUTPUT_BUCKET
import os


def upload_blob(bucket, source, dest):
    bucket = client.get_bucket(bucket)
    
    print('\n [INFO] Start Upload {} to {}.'.format(source, dest))
        
    blob = bucket.blob(dest)
    blob.upload_from_filename(source)
    blob.make_public()

    print('\n [INFO] Finish upload {} to {}.'.format(source, dest))
    return blob.public_url


def upload_output(source_path):
    filename = os.path.basename(source_path)
    return upload_blob(IMG_PROCESS_OUTPUT_BUCKET, source_path, filename)

if (__name__ == '__main__'):
    url = upload_output('img_processor/dataset/searchee.1.0.png')
    print(url)
