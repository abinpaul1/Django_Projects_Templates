import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Pro.settings')

import django
django.setup()

import random
from ProApp.models import User
from faker import Faker

fakegen = Faker()

def populate(N = 5):
    for i in range(N):
        first = fakegen.first_name()
        last = fakegen.last_name()
        f_email = fakegen.email()

        user_details = User.objects.get_or_create(first_name = first, last_name = last , email = f_email )[0]

if __name__ == '__main__':
    populate(25)
    print("Populated")
