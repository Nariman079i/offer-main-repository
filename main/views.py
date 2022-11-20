
from main.serializers import *
from main.models import *
from django.shortcuts import render, HttpResponse
from dadata import Dadata
from json import *
from rest_framework.generics import *
from rest_framework.views import *
from rest_framework.permissions import *


class FullProfileCreate(CreateAPIView, ListAPIView):
    queryset = TestProfile.objects.all()
    serializer_class = TestSerializer
    permission_classes = (IsAuthenticated,)


class ProfileApiCreate(ListAPIView, CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerialiser

class ProfileApiView(ListAPIView):
    def get_queryset(self):
        role = self.kwargs.get('role')
        limit = self.kwargs.get('limit')
        return Profile.objects.filter(role=role)[:limit]
    serializer_class = ProfileSerialiser

class ProfileApiList(ListAPIView):
    def get_queryset(self):
        role = self.kwargs.get('role')
        return Profile.objects.filter(role=role)
    serializer_class = ProfileSerialiser





class UserApiList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRegistrationList(ListAPIView, CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer





class UserLoginApi(APIView):
    def get(self,request):
        #При входе пользователь получает все аpi которые принадлежат пользователю
        pass
    def post(self,request):
        pass
def index(request):
    file = 'main/index.html'
    context = {
        'title':'Артур КНЧНЫЙПЕТХ'
    }
    return render(request,file,context=context)



def get_inn_user(request, inn):
    token = "d4cbcec638775b2531d59feab5387d70c32d420b"
    dadata = Dadata(token)
    file = 'main/inn.html'
    result = dadata.find_by_id("party", inn)
    data = dumps(result , indent=4 , ensure_ascii=False , sort_keys=False, separators=(',' , ':'))
    print(data , type(data))
    return HttpResponse(data,content_type="application/json")


