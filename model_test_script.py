import datetime as dt
from users.models import User
from searches.models import *

u1 = User(full_name='SpiderMan', dob=dt.date(1997, 9, 12), email_id='spider@example.com', ph_num='9876543434')
u1.save()
u2 = User(full_name='BatMan', dob=dt.date(1997, 9, 12), email_id='bat@example.com', ph_num='9876543412')
u2.save()

comp1 = Complaint(name='Missing Robin', submitter=u1, poi='Batcave', doi=dt.date(2019, 3,15), status=Complaint.WAITING_FOR_APPROVAL)
comp1.save()

comp2 = Complaint(name='Missing Joker', submitter=u2, poi='Gotham', doi=dt.date(2019, 3,15), status=Complaint.APPROVED)
comp2.save()

sche1 = Searchee(full_name='Robin Hodo', complaint=comp1, dob=dt.date(1999, 12, 1))
sche1.save()

saml1 = SearcheeSample(searchee=sche1, image_url='www.example.com/imag1.jpg')
saml1.save()

saml2 = SearcheeSample(searchee=sche1, image_url='www.example.com/imag2.jpg')
saml2.save()

srch1 = Search(searchee=sche1, name='Search in batcave 1', video='www.example.com/vid1.mp4')
srch1.save()

srch2 = Search(searchee=sche1, name='Search in batcave 2', video='www.example.com/vid1.mp4')
srch1.save()

res1 = SearchResult(search=srch1, timestamp_sec=12)
res1.save()
res2 = SearchResult(search=srch1, timestamp_sec=27)
res2.save()

u1.complaints.get()