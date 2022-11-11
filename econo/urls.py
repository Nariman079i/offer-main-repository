from django.urls import path
from econo.views import *

urlpatterns = [
    path('get/exp/' , GetExpense.as_view()),
    path('get/inc/' , GetIncome.as_view()),
    path('post/exp/' , CreateExpense.as_view()),
    path('post/inc/' , CreateIncome.as_view()),

]

