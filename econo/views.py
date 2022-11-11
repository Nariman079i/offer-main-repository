from rest_framework.serializers import ModelSerializer

from econo.models import *
from rest_framework.generics import *

class ExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class IncomeSerializer(ModelSerializer):
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