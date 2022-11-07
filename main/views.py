from django.shortcuts import render

# Create your views here.
def index(request):
    file = 'main/index.html'
    context = {
        'title':'Артур чмо'
    }
    return render(request,file,context=context)