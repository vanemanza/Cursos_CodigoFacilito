from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    contexto = {
        'mensaje' : 'Listado de Productos ',
        'titulo' : 'Productos',
        'productos': [
            {'titulo': 'Playera', 'precio': 5, 'stock': True},
            {'titulo': 'Camisa', 'precio': 7, 'stock': True},
            {'titulo': 'Mochila', 'precio': 20, 'stock': False}, #producto
            {'titulo': 'Laptop', 'precio': 200, 'stock': True}, #producto

        ]
    }
    return render(request, 'index.html', contexto)

