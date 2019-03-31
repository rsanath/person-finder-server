import requests
import os
import cv2
import numpy as np
from PIL import Image
import os
from .face_recogniser import FaceRecogniser


#
#   This module has two applications
#   Downloads and feed images as input to a ML model for training
#   Given a video recognize faces in it
#
class ImageProcessor:
    dataset_path = 'img_processor/dataset'

    haar_cascade_path = 'img_processor/haarcascade_frontalface_default.xml' 
    
    detector = cv2.CascadeClassifier(haar_cascade_path)
    recogniser = FaceRecogniser()

    def add_searchee(self, ids, images):
        for i in range(len(ids)):
            self.fetch_searchee_images(ids[i], images[i])
        
        faces, ids = self.get_train_data()
        self.recogniser.train_model(faces, ids)
        print("\n [INFO] {0} faces trained.".format(len(np.unique(ids))))


    def find_searchee(self, video_url):
        results = self.recogniser.process_video(video_url)
        return results


    def fetch_searchee_images(self, searchee_id, images):
        os.makedirs(self.dataset_path, exist_ok=True)

        for i in range(len(images)):
            img_dest = self.dataset_path + '/searchee.{}.{}.png'.format(searchee_id, i)
            image_url = images[i]
            try:
                response = requests.get(image_url)
            except:
                print('\n [ERROR] Error retriving resource at {}'.format(image_url))
                continue
            
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

    def clear_generated_data(self):
        pass


def test():
    obama_id = 1
    obama = 'Obama'
    obama_images = [
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
    
    
    nawas_id = 2
    nawas = 'Nawas'
    nawas_images = [
        'https://img.timesnownews.com/story/1553595476-NAwaz_Sharif_IANS_6.jpg?d=600x450',
        'https://arynews.tv/wp-content/uploads/2019/03/Nawaz-Sharif-750x369.jpg',
        'https://www.devdiscourse.com/remote.axd?https://devdiscourse.blob.core.windows.net/devnews/09_02_2019_14_56_08_8769178.png?width=920',
        'https://www.geo.tv/assets/uploads/updates/2018-12-25/223044_8738561_updates.jpg',
        'https://images.news18.com/ibnlive/uploads/2017/04/nawaz-sharif-reuters-875.gif',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfQWBARdpomYgbKTxyO5b8lq9BQK6dB0XE-_9MH1EK7d70SnED',
        'https://enews.hamariweb.com/wp-content/uploads/2019/03/Nawaz-Sharif.jpg',
        'https://images.news18.com/ibnlive/uploads/382x253/jpg/2016/04/nawaz-sharif.jpg',
        'https://www.samaa.tv/wp-content/uploads/2018/07/Mr-Nawaz-AFP-640x428.jpg',
        'https://img.etimg.com/thumb/msid-64885293,width-1200,height-900,resizemode-4,imgsize-148200/nawaz-sharif-getty.jpg',
        'http://www.aaj.tv/wp-content/uploads/2018/03/nawazsharif-960x540.jpg',
    ]
    

    video = 'https://r5---sn-a5mlrnek.googlevideo.com/videoplayback?lmt=1531632726351526&pl=22&id=o-AFleIYzOtS2ns9dM1lHa09T84z49oW_uG3dUMRZ4oqSN&dur=165.720&mt=1553970889&mv=m&ms=au%2Conr&ip=173.232.7.122&mm=31%2C26&mn=sn-a5mlrnek%2Csn-n4v7knlz&ipbits=0&ratebypass=yes&signature=0FD2C1E86327635D5EC722927ABA1F513706B06B.29DA9D31E97AA930588A7C4271A125765F1FABA8&requiressl=yes&sparams=dur%2Cei%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cexpire&initcwndbps=9981250&fvip=5&itag=22&source=youtube&mime=video%2Fmp4&key=yt6&expire=1553992591&c=WEB&ei=L7efXLGiBY6DkgbK94XABg&video_id=MS5UjNKw_1M&title=President+Obama%27s+best+speeches'

    # s = Search(searchee=robin, video='http://s000.tinyupload.com/download.php?file_id=83612465169586447527&t=8361246516958644752730766')

    processor = ImageProcessor()

    processor.add_searchee([obama_id, nawas_id], [[], []])
    results = processor.find_searchee(video)

if (__name__ == '__main__'):
    test()