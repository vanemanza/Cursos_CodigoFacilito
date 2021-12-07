from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('nuevo', views.mascota, name="nuevo"),
    path('listar', views.listado, name="listar"),
]