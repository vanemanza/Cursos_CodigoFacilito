from django import forms

from .models import Mascota

class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota

        fields = '__all__'

        labels = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad_aproximada': 'Edad aproximada',
            'fecha_rescate': 'Fecha de rescate',                
            'foto': 'Foto',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_rescate': forms.TextInput(attrs={'class': 'form-control'}),          
            'foto': forms.FileInput(),
        }
        

