from django.shortcuts import render
from .models import Ciclo

# Create your views here.
def index(request):
    #context = {}
    ciclo_list = Ciclo.objects.all()
    return render(request, 'index.html', context={})

def ciclo(request):
    ciclo_list= Ciclo.objects.all()
    return render(request, 'ciclos.html', context={'ciclo_list': ciclo_list})
