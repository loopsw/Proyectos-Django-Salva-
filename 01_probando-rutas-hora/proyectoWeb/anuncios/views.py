from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
#def home(request):
#    return HttpResponse('Hola mundo!')

def hora_actual(request):
    hora_actual = datetime.datetime.now() 
    mensaje = """
        <html>
        <head>
            <title>Mi pagina con django</title>
        </head>
        <body>
            <h1> La hora actual es {}
        </body>
        </html>""".format(hora_actual.strftime("%Y/%m/%d"))
    return HttpResponse(mensaje)

def edad(request,year):
    mensaje = "Usted tiene {} años".format(2021-year)
    return HttpResponse(mensaje)