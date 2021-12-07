from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):

    return render(request, 'mascota/index.html', {})

def form_alta(request):

    return render(request, 'mascota/mascota_form.html', {})    

