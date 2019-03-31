import datetime as dt

from faker import Faker

from users.models import User
from searches.models import *


fake = Faker()

modi = User(
    full_name='Narendra Modi',
    dob=dt.date(2019, 9, 17),
    sex=User.MALE,
    email_id='modi@example.com',
    ph_num='3546453645',
    password='password',
    address='Varanasi',
    image_url='https://upload.wikimedia.org/wikipedia/commons/9/90/PM_Modi_2015.jpg',
    type=User.CLIENT
)
modi.save()


complaint = Complaint(
    doi=dt.date(2019, 2, 15),
    poi='Pheonix Mall',
    submitter=modi
)
complaint.save()


rahul = Searchee(
    full_name='Rahul Gandhi',
    dob=dt.date(1970, 6, 19),
    sex=User.MALE,
    complaint=complaint
)
rahul.save()


rahul_images = [
    'https://bsmedia.business-standard.com/_media/bs/img/article/2019-03/26/full/1553613763-2265.jpg',
    'https://www.hindustantimes.com/rf/image_size_960x540/HT/p2/2019/03/28/Pictures/aicc-obc-national-convention_ab3ebe10-514c-11e9-a540-e59d8ae6a1ea.jpg',
    'https://img.etimg.com/thumb/msid-68653440,width-1200,height-900,resizemode-4,imgsize-304652/rahul-gandhi.jpg',
    'https://img.etimg.com/thumb/msid-68540983,width-300,imgsize-99231,resizemode-4/rahul-gandhi1_pti.jpg',
    'https://resize.khabarindiatv.com/resize/newbucket/715_-/2019/03/pti12-14-2018-000151b-1554010920.jpg',
    'https://indiablooms.com/news_pic/2019/1-1553594605.jpg',
    'https://static-news.moneycontrol.com/static-mcnews/2019/03/Rahul-gandhi_Congress-770x433.jpg',
    'https://i10.dainikbhaskar.com/thumbnails/730x548/web2images/www.bhaskar.com/2019/02/13/0521_phpthumb_generated_thumbnail_17.jpeg',
    'https://www.thenewsminute.com/sites/default/files/styles/news_detail/public/Rahul%20Gandhi%20Facebook%203x2_0.jpg?itok=SM0jfgTV',
    'https://theprint.in/wp-content/uploads/2019/03/Rahul-Gandhi-Congress-chief-1280x720.jpg',
    'https://images.livemint.com/rf/Image-621x414/LiveMint/Period2/2019/01/17/Photos/Processed/rahul-gandhi-kDEI--621x414@LiveMint.jpg',
    'https://pbs.twimg.com/profile_images/974851878860312582/O-Zn2b72_400x400.jpg',
    'https://images.firstpost.com/wp-content/uploads/2019/03/rahul-gandhi-380-PTI.jpg',
    'https://img.etimg.com/thumb/msid-68546617,width-1200,height-900,resizemode-4,imgsize-90316/rahul-gandhi-pti-5.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Rahul_Gandhi.jpg/220px-Rahul_Gandhi.jpg',
    'https://images.mid-day.com/images/2018/jul/Rahul-Gandhi-CWC_d.jpg'
]
for i in rahul_images:
    sample = SearcheeSample(
        searchee=rahul,
        image_url=i
    )
    sample.save()


vid = 'https://r1---sn-4g5edn7y.googlevideo.com/videoplayback?mime=video%2Fmp4&expire=1554050116&sparams=dur%2Cei%2Cid%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cexpire&mt=1554027701&itag=22&ipbits=0&c=WEB&ratebypass=yes&fvip=1&pl=21&ip=178.77.98.118&requiressl=yes&lmt=1553513436560455&ms=au%2Crdu&source=youtube&mv=u&dur=84.822&id=o-AEkCaZ1oWVCiEr1nk3UPK_6BFEgSbFBJzz44rFONDlK-&signature=81D3753D8383B608661EEE5024415CB073BF69D1.8F32B61995D09F2148C4433A4BB2AEF65814364E&key=yt6&mm=31%2C29&mn=sn-4g5edn7y%2Csn-4g5e6nl7&ei=5JegXPeIFdqb1gL-qoagDQ&txp=5432432&video_id=KYg2HU5SOGk&title=Poorest+20%25+Families+to+Get+Rs+72%2C000+Per+Year-+Rahul+Gandhi'
search = Search(
    searchee=rahul,
    video_url=vid
)