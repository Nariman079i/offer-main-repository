from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from random import randint
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


# Create your views here.
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


def send(request):

    if request.method == "POST":
        code = randint(100000,999999)
        user = [request.data.get('recipient')]
        msg = render_to_string('email_confirmation/send.html', {'code': code})
        send_mail('Offer - Подтверждение аккаунта', msg, settings.EMAIL_HOST_USER, user , html_message=msg)
        return HttpResponse("Post response Success!!")
    elif request.method == "GET":
        return HttpResponse('Get response Success!!')
