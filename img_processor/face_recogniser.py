import os
import uuid
import cv2
import numpy as np
from . import util



OUTPUT_IMG_WIDTH = 600


def mkdir_path(path):
    if not os.access(path, os.F_OK):
        print('\n [INFO] create directory {}'.format(path))
        os.mkdir(path)

class FaceRecogniser:
    output_path = 'img_processor/outputs/'
    trainer_path = 'img_processor/trainer/'
    haar_cascade_path = 'img_processor/haarcascade_frontalface_default.xml'
    
    detector = cv2.CascadeClassifier(haar_cascade_path)
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    font = cv2.FONT_HERSHEY_SIMPLEX

    def __init__(self):
        mkdir_path(self.output_path)
        mkdir_path(self.trainer_path)

    def train_model(self, faces, ids):
        trainer_file = self.trainer_path + 'trainer.yml'

        if os.path.isfile(trainer_file):
            self.recognizer.read(trainer_file)
            
        self.recognizer.train(faces, np.array(ids))
        self.recognizer.save(trainer_file)


    def process_video(self, video_url):
        results = []

        vid = cv2.VideoCapture(video_url)
        vid.set(3, 640)  # set video widht
        vid.set(4, 480)  # set video height

        minW = 0.1*vid.get(3)
        minH = 0.1*vid.get(4)

        frames_processed = 0
        step = 100
        
        success, img = vid.read()
        while success:            
            success, img = vid.read()

            timestamp = vid.get(cv2.CAP_PROP_POS_MSEC) / 1000
            frame = vid.get(cv2.CAP_PROP_POS_FRAMES)
            
            if frame % step != 0:
                continue

            frames_processed += 1

            # display the time 
            cv2.putText(img, str(timestamp), (30, 30), self.font, 1, (255, 255, 255), 2)
            
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = self.detector.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(minW), int(minH)),
            )

            for(x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                id, confidence = self.recognizer.predict(gray[y:y+h, x:x+w])

                confidence_text = "  {0}%".format(round(100 - confidence))

                if (confidence < 100):
                    cv2.putText(img, str(id), (x+5, y-5), self.font, 1, (255, 255, 255), 2)
                    cv2.putText(img, str(confidence_text), (x+5, y+h-5), self.font, 1, (255, 255, 0), 1)
                    
                    snap_path = self.output_path + str(uuid.uuid4()) + '.png'
                    print('\n [INFO] Writing frame at {}'.format(snap_path))
                    
                    try:
                        cv2.imwrite(snap_path, util.resize(img, width=OUTPUT_IMG_WIDTH))
                    except:
                        snap_path = None
                        print('\n [ERROR] Unable to write frame at {}'.format(snap_path))

                    results.append(
                        dict(
                            searchee_id=id,
                            confidence=round(100 - confidence),
                            timestamp=timestamp,
                            image=snap_path,
                            x1=x,
                            y1=y,
                            x2=x+w,
                            y2=y+h
                        )    
                    )

        print('\n [INFO] Processed video {}'.format(video_url))
        print('\n [INFO] Processed {} frames'.format(frames_processed))
        print('\n [INFO] # of results generated = {}'.format(len(results)))

        return results
