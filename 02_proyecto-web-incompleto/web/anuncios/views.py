from django.shortcuts import render
from .models import Anuncio
from django.http import HttpResponse

# Create your views here.
def mostrarImagen(request):
    return render(request,'index.html',{})
    
    
def mostrarAnuncios(request):
    anuncios = Anuncio.objects.filter(state="publicado")
    #return HttpResponse(anuncios)
    return render(request,'anuncios.html',{'anuncios':anuncios})

def mostrarIndex(request):
    return render(request,'index.html')