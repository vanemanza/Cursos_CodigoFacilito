from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def adopcion(request):
    mensaje = "hola persona q adopta"
    return HttpResponse(mensaje)