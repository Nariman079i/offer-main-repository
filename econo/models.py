from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import *

class Expense(Model):

    name = CharField(max_length=60)
    sum = FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10000000000.0 , message="dsagdf")],max_length=255)
    date = DateField()
    operation = CharField(max_length=60,default="Расходы", editable=False)

class Income(Model):

    name = CharField(max_length=60)
    sum = FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10000000000.0)],max_length=255)
    date = DateField()
    operation = CharField(max_length=60,default="Доходы", editable=False)
