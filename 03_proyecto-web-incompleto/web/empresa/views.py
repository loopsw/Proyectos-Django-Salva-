from django.shortcuts import render

# Create your views here.
def mostrarEmpresa(request):
    return render(request,'empresa/index.html')