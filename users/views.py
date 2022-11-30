from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.

class AuthenticatedUser(APIView):
    def post(self, request):
        email = self.request.data.get('email')
        password = self.request.data.get('password')
        user = authenticate(email=email,password=password)
