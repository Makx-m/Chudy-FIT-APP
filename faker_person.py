import os
import django
import random
from faker import Faker


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chudyproject.settings')
django.setup()

from chudyapp.models.PersonModel import Person

def persons(N=1_000):
    fake = Faker()

    for _ in range(N):
        name = fake.name()
        weight = random.randint(60, 200)
        height = random.randint(130, 210)
        sex = random.choice([1, 2])
        age = random.randint(18, 60)
        activePerDay = random.randint(0, 3)

        person = Person(name=name, weight=weight, height=height, sex=sex, age=age, activePerDay=activePerDay)
        person.save()


if __name__ == '__main__':
    print('Wgrywanie przykladowych danych')
    persons()
    print('Zakonczono wgrywanie danych')