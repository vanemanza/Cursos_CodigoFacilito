#from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from .models import Company

# Create your views here.

class CompanyView(View):

    def get(self, request):
        companies = list(Company.objects.values())
        if len(companies)>0:
            datos = {'message': 'Success', 'companies': companies}
        else:
            datos = {'message': 'Companies not found ...'}
        return JsonResponse(datos)    
       
    def post(self, request):
        datos = {'message': 'Success'}

    def put(self, request):
        pass

    def delete(self, request):
        pass    