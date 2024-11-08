import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','funeducare.settings')

import django
django.setup()

#fake pop script
import random
from aplikasi_pertama.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ["Social", "Search", "Marketplace", "News", "Games"]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # GET THE TOPIC FOR THE ENTRY
        top = add_topic()
        #CREATE FAKE DATA
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        #CREATE BEW WEBPAGE ENTRY
        webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name=fake_name)[0]
        #CREATE FAKE ACCESS RECORD
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]
       
if __name__ == '__main__':
    print("Populating script....")
    populate(20)
    print("rampung") 
