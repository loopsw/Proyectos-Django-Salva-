# Utilities
from datetime import datetime
#Django
from django.http import HttpResponse
# json
import json

def holaMundo(request):
    now  = datetime.now().strftime('%b %d, %Y - %H:%M')
    return HttpResponse("Hola mundo!, la fecha es {}".format(str(now)))

def sort_integers(request):
    """ Returns a JSON response with sorted integers"""
    numbers = [int(i) for i in request.GET['numeros'].split(',')]
    numbers_sorted = sorted(numbers)
    data = {
        'status':'ok',
        'numbers': numbers_sorted,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(json.dumps(data),content_type="application/json")

def say_hi(request,nombre,edad):
    if edad < 12:
        message = "Sorry {}, you are not allowed here".format(nombre)
    else:
        message = "Hello, {}! Welcome to platzigram".format(nombre)
    return HttpResponse(message)
