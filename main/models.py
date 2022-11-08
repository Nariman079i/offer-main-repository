from django.db.models import *
from main.admin import *
# Create your models here.
class Profile(Model):

    role = ((1, "Инвестор"),
            (2, "Предприниматель"),
            (3,'Компания'))
    name = CharField(max_length=30)
    img = ImageField(upload_to='img/')
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    industry = CharField(max_length=40)
    status = CharField(max_length=80)

    role = CharField(max_length=30,choices=role)
    def __str__(self):
        return self.name

admin.site.register(Profile)