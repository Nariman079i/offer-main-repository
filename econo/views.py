from rest_framework import serializers
from django.core.validators import *
from econo.models import *
from rest_framework.generics import *

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

    def validate(self, data):
        errors = []
        if data['sum'] == 0:
            errors.append({'sum': 'Сумма не должна быть равным 0'})
        if data['name'] == "":
            errors.append({'name': 'Длина поля Name не должна превышать 60 символов'})

        if errors:
            raise serializers.ValidationError({'errors':errors})
        return data

class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = '__all__'


class CreateExpense(CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class CreateIncome(CreateExpense):
    queryset = Expense.objects.all()
    serializer_class = IncomeSerializer

class GetExpense(ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class GetIncome(ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = IncomeSerializer