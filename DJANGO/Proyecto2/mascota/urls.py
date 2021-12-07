from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('form', views.form_alta, name="form_alta"),
]