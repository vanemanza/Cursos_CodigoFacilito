from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {
        'mensaje' : 'Nuevo mensaje desde la vista',
        'titulo' : 'index',
    })