import requests
import os
import cv2
import numpy as np
from PIL import Image
import os
import uuid
from .face_recogniser import FaceRecogniser


class ImageProcessor:
    dataset_path = 'img_processor/dataset'
    output_path = 'img_processor/outputs'

    haar_cascade_path = 'img_processor/haarcascade_frontalface_default.xml' 
    
    detector = cv2.CascadeClassifier(haar_cascade_path)
    recogniser = FaceRecogniser()

    def add_searchee(self, id, images):
        self.fetch_searchee_images(id, images)
        
        images, ids = self.get_train_data()
        self.recogniser.train_model(images, ids)
        print("\n [INFO] {0} faces trained.".format(len(np.unique(ids))))


    def find_searchee(self, video_url):
        resuts = self.recogniser.process_video(video_url)


    def fetch_searchee_images(self, searchee_id, images):
        os.makedirs(self.dataset_path, exist_ok=True)

        for i in range(len(images)):
            img_dest = self.dataset_path + '/searchee.{}.{}.png'.format(searchee_id, i)
            image_url = images[i]
            response = requests.get(image_url)
            
            print("\n [INFO] Download {} to {}".format(image_url, img_dest))

            with open(img_dest, 'wb') as f:
                f.write(response.content)


    def get_train_data(self):
        image_paths = [os.path.join(self.dataset_path, f) for f in os.listdir(self.dataset_path)]
        
        face_samples = []
        ids = []
        
        for image_path in image_paths:
            PIL_img = Image.open(image_path).convert('L')  # convert it to grayscale
            img_numpy = np.array(PIL_img, 'uint8')
            
            id = int(os.path.split(image_path)[-1].split(".")[1]) # get the searchee id

            faces = self.detector.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                face_samples.append(img_numpy[y:y+h, x:x+w])
                ids.append(id)

        return face_samples, ids    


def test():
    searchee_id = 1
    searchee_name = 'Obama'

    id_name_dict = {
        str(searchee_id): searchee_name 
    }

    images = [
        'https://www.whitehouse.gov/wp-content/uploads/2017/12/44_barack_obama1.jpg',
        'https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTE4MDAzNDEwNzg5ODI4MTEw/barack-obama-12782369-1-402.jpg',
        'https://timedotcom.files.wordpress.com/2017/12/barack-obama.jpeg',
        'https://images-na.ssl-images-amazon.com/images/I/61n2ctN6jBL._SX425_.jpg',
        'https://i.imgur.com/KYsNypm.jpg',
        'https://static.turbosquid.com/Preview/2014/07/10__12_46_11/Obama_Both_heads_morph_whight_b_01.png2a7b88a1-d678-4c9c-9406-4ba0b3200289Original.jpg',
        'https://npg.si.edu/sites/default/files/blog_obama_martin_schoeller.jpg',
        'https://i.dailymail.co.uk/i/pix/2013/08/03/article-2384045-1729E0D2000005DC-553_634x428.jpg',
        'https://www.askideas.com/media/38/Obama-With-Sad-Face-Funny-Picture.jpg',
        'https://www.dcclothesline.com/wp-content/uploads/2013/08/funny-obama-faces-strange-0.jpg?w=640',
        'https://www.markyfresh.com/wp-content/uploads/2018/09/Obama-Remix-1-compressed.jpg',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxIdJDpUX2uNHQtIgbTS6-24a3wayGotyhiETMf_h7tii9V2UsJg',
        'https://granitegrok.com/wp-content/uploads/2013/04/obama-angry.jpg',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSX0gHZbrMStNQqxmXLK4rFfVJaHifRw5U9nL7aeARPYrw9o27rAA',
        'https://www.gannett-cdn.com/media/USATODAY/theOval/2012/10/10/ap-obama-2012_182-16_9.jpg?width=580&height=326&fit=crop',
        'http://www.teapartytribune.com/wp-content/uploads/2011/10/Obama-face.png',
        'https://i0.wp.com/cdn02.cdn.justjared.com/wp-content/uploads/2016/03/obama-faces/president-michelle-obama-make-amazing-faces-during-story-time-02.jpg?w=600',
        'https://whitehouse.gov1.info/photos_obama_face/obama-happy-flag.jpg',
        'http://www.alternavox.net/wp-content/uploads/7943-el-presidente-de-estados-unidos-barack-obama-en-conferencia-.jpg',
        'https://static01.nyt.com/images/2011/07/31/sunday-review/FACES/FACES-jumbo.jpg',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEPfkLein0Rtn2m9GlMUgF91hAofg5iiy0K-CUPSHOtxNr-86U',
        'https://pixel.nymag.com/imgs/daily/intelligencer/2016/01/05/05-barack-obama-crying-1.w700.h700.jpg',
        'https://cbsnews1.cbsistatic.com/hub/i/2011/07/29/73d3fbf0-a643-11e2-a3f0-029118418759/obama_AP11072901970.jpg',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0CBIovLs9ryJXK9WSkzIOGf-zcxkBBEyO0Ci1SbIzf1swtLC2qw',
        'https://parade.com/wp-content/uploads/2013/08/obama-face-forward-ftr.jpg',
        'https://bloximages.newyork1.vip.townnews.com/stltoday.com/content/tncms/assets/v3/editorial/f/3e/f3e097cc-7f43-5acb-8c94-2e3892e59168/582b2c90b7387.image.jpg',
        'https://media.fox32chicago.com/media.fox32chicago.com/photo/2015/10/12/101215_SR_ThirdTerm_1280_1444692321094_349523_ver1.0_640_360.jpg',
    ]
    images = []
    video = 'https://dl4.volafile.net/get/CGEiuLuKhoCW4/obama_vid.mp4'
    
    processor = ImageProcessor()

    processor.add_searchee(searchee_id, images)
    processor.find_searchee(video)

test()