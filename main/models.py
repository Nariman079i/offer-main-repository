from django.db.models import *
# Create your models here.
class Profile(Model):

    role = (("investor", "investor"),
            ("businessman", "businessman"),
            ("company",'company'))
    name = CharField(max_length=30)
    img = ImageField(upload_to='img/')
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    industry = CharField(max_length=40)
    status = CharField(max_length=80)

    role = CharField(max_length=30,choices=role)
    def __str__(self):
        return self.name

