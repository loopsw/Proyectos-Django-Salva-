from django.shortcuts import render
from .models import Anuncio
# Create your views here.
def index(request):
    return render(request,'index.html')

def anuncios(request):
    anuncios = Anuncio.objects.filter(status='publicado')
    return render(request,'anuncios.html',{'anuncios':anuncios})