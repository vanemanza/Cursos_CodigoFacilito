from django.shortcuts import render, redirect
from .models import Mascota
from .forms import MascotaForm

#from django.http import HttpResponse

# Create your views here.
def index(request):

    return render(request, 'mascota/index.html', {})

def mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')    
    else:
        form = MascotaForm()   

    return render(request, 'mascota/mascota_form.html', {'form': form})    

def listado(request):
    mascotas = Mascota.objects.all()
    contexto = {'mascotas': mascotas}
    return render(request, 'mascota/mascota_list.html', contexto)