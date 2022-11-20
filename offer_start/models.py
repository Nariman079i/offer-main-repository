from django.db.models import *
from django.contrib.auth.models import User


class Investor(Model):

    user = OneToOneField(User, on_delete=CASCADE , related_name='investor')
    inn = CharField(max_length=12)
    call_number = CharField(max_length=60)
    name = CharField(max_length=60)
    surname = CharField(max_length=60)
    birth_date = DateField()

    locate = CharField(max_length=255)
    industry = CharField(max_length=255)
    sub_industry = CharField(max_length=255)

    status = CharField(max_length=60)
    gender = CharField(max_length=12)


class Bussinessmen(Model):

    user = OneToOneField(User, on_delete=CASCADE, related_name='bussinessmen')

    inn = CharField(max_length=12)
    call_number = CharField(max_length=60)
    name = CharField(max_length=60)
    surname = CharField(max_length=60)
    birth_date = DateField()

    locate = CharField(max_length=255)
    industry = CharField(max_length=255)
    sub_industry = CharField(max_length=255)

    status = CharField(max_length=60)
    gender = CharField(max_length=12)


class Company(Model):
    user = OneToOneField(User, on_delete=CASCADE , related_name='company')

    inn = CharField(max_length=12)
    call_number = CharField(max_length=60)
    name = CharField(max_length=60)

    create_date = DateField()
    url = CharField(max_length=255)
    locate = CharField(max_length=255)
    industry = CharField(max_length=255)


    status = CharField(max_length=60)
    about = CharField(max_length=500)