from django.shortcuts import render, HttpResponse
from dadata import Dadata
from json import *
# Create your views here.
def index(request):
    file = 'main/index.html'
    context = {
        'title':'Артур XHttpResponse'
    }
    return render(request,file,context=context)



def get_inn_user(request, inn):
    token = "d4cbcec638775b2531d59feab5387d70c32d420b"
    dadata = Dadata(token)
    file = 'main/inn.html'
    result = dadata.find_by_id("party", inn)
    if len(result) <= 0:
        data = "Taкого ИНН не существует"
    else:
        data = dumps(result, indent=4 , ensure_ascii=False)
    return HttpResponse(dumps(result , indent=4 , ensure_ascii=False , sort_keys=False, separators=(',' , ':')), content_type="application/json")
