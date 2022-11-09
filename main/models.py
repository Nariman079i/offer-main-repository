from django.db.models import *
from main.admin import *
# Create your models here.
class Profile(Model):

    role = (('inv', "Инвестор"),
            ('bus', "Предприниматель"),
            ('com','Компания'))
    name = CharField(max_length=30)
    img = ImageField(upload_to='img/')
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    industry = CharField(max_length=40)
    locate = CharField(max_length=40, null=True)
    status = CharField(max_length=80)

    role = CharField(max_length=30,choices=role)
    def __str__(self):
        return self.first_name.__str__() + self.last_name.__str__()


admin.site.register(Profile , ProfileAdmin)
