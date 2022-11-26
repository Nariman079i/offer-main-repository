from django.contrib.auth.models import User
from django.db.models import *
from django.core.validators import *

from clean.admin import admin

class Image(Model):
    title = CharField(max_length=60, null=True)
    img = ImageField(upload_to='details/')


class Product(Model):
    user = ForeignKey(User, on_delete=CASCADE, default=1)
    title = CharField(max_length=50)
    count = PositiveIntegerField()
    price = FloatField(max_length=255,
                       validators=[
                           MaxValueValidator(50000.0,message="Цена не должна превышать 50000р"),
                           MinValueValidator(0.1,message="Цена не должна быть меньше 0р")
                       ])
    description = TextField()

    def __str__(self):
        return self.title

