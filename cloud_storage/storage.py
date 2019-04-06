from . import client
from . import IMG_PROCESS_OUTPUT_BUCKET, SEARCHEE_SAMPLE_BUCKET, FIR_BUCKET
import os



def upload_blob_from_file(bucket, src_file, dest):
    bucket = client.get_bucket(bucket)
    
    print('\n [INFO] Start Upload {} to {}.'.format(src_file.name, dest))
    
    blob = bucket.blob(dest)
    blob.upload_from_file(src_file)
    
    print('\n [INFO] Finish upload {} to {}.'.format(src_file.name, dest))

    blob.make_public()
    return blob.public_url

def upload_blob_from_filename(bucket, source, dest):
    bucket = client.get_bucket(bucket)
    
    print('\n [INFO] Start Upload {} to {}.'.format(source, dest))
        
    blob = bucket.blob(dest)
    blob.upload_from_filename(source)
    blob.make_public()

    print('\n [INFO] Finish upload {} to {}.'.format(source, dest))
    return blob.public_url

def upload_fir(file):
    filename = os.path.basename(file.name)
    return upload_blob_from_file(FIR_BUCKET, file, filename)

def upload_sample_image(file):
    filename = os.path.basename(file.name)
    return upload_blob_from_file(SEARCHEE_SAMPLE_BUCKET, file, filename)

def upload_output(source_path):
    filename = os.path.basename(source_path)
    return upload_blob_from_filename(IMG_PROCESS_OUTPUT_BUCKET, source_path, filename)

# for testing
if (__name__ == '__main__'):
    with open("/Users/sanath/Downloads/bg.png", "rb") as f:
        url = upload_blob_from_file(SEARCHEE_SAMPLE_BUCKET, f, 'test2.png')
        print(url)