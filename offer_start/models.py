from django.db.models import *
from django.contrib.auth.models import User


class Investor(Model):

    user = OneToOneField(User, on_delete=CASCADE , related_name='investor')
    inn = CharField(max_length=12, blank=True, null=False )
    call_number = CharField(max_length=60, blank=True, null=False)

    avatar = ImageField(upload_to='img/', null=True)

    name = CharField(max_length=60, blank=True, null=False)
    surname = CharField(max_length=60, blank=True, null=False)
    birth_date = DateField(blank=True, null=False)

    locate = CharField(max_length=255, blank=True, null=False)
    industry = CharField(max_length=255, blank=True, null=False)
    sub_industry = CharField(max_length=255, blank=True, null=False)

    status = CharField(max_length=60, blank=True, null=False)
    gender = CharField(max_length=12, blank=True, null=False)


class Bussinessmen(Model):

    user = OneToOneField(User, on_delete=CASCADE, related_name='bussinessmen')

    avatar = ImageField(upload_to='img/', null=True)

    inn = CharField(max_length=12, blank=True, null=False)
    call_number = CharField(max_length=60, blank=True, null=False)
    name = CharField(max_length=60, blank=True, null=False)
    surname = CharField(max_length=60, blank=True, null=False)
    birth_date = DateField( blank=True, null=False)

    locate = CharField(max_length=255, blank=True, null=False)
    industry = CharField(max_length=255, blank=True, null=False)
    sub_industry = CharField(max_length=255, blank=True, null=False)

    status = CharField(max_length=60, blank=True, null=False)
    gender = CharField(max_length=12, blank=True, null=False)


class Company(Model):
    user = OneToOneField(User, on_delete=CASCADE , related_name='company')

    avatar = ImageField(upload_to='img/',null=True)

    inn = CharField(max_length=12, blank=True, null=False)
    call_number = CharField(max_length=60, blank=True, null=False)
    name = CharField(max_length=60, blank=True, null=False)

    create_date = DateField( blank=True, null=False)
    url = CharField(max_length=255, blank=True, null=False)
    locate = CharField(max_length=255, blank=True, null=False)
    industry = CharField(max_length=255, blank=True, null=False)

    status = CharField(max_length=60, blank=True, null=False)
    about = CharField(max_length=500, blank=True, null=False)

class Image(Model):
    title = CharField(max_length=60, null=True)
    img = ImageField(upload_to='details/')

class Service(Model):
    title = CharField(max_length=60)
    img = ForeignKey(Image, on_delete=PROTECT, null=True, related_name='image')
    service_type = ForeignKey('ServiceType', on_delete=CASCADE , related_name='type')

class ServiceType(Model):
    code = CharField(max_length=20)
    title = CharField(max_length=255)


