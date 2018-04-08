import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Shubham_WebTech.settings")

import django

django.setup()
import random
from NutritionManagement.models import Nutrients
from faker import Faker
fakeGen = Faker()


def populate(N):
    for i in range(N):
        fake_name = fakeGen.name()
        fake_url = fakeGen.url()
        fake_date = fakeGen.date()
        t = topic()
        w = WebPage.objects.get_or_create(
            topic=t, name=fake_name, url=fake_url)[0]
        w.save()
        acc_record = AccessRecord.objects.get_or_create(
            name=w, date=fake_date)[0]
        acc_record.save()

if __name__ == '__main__':
    print("Populating")
    populate(15)
    print("Populated")