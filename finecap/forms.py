from django.forms import ModelForm
from .models import Reservas
from django import forms


class ReservaForm(ModelForm):

    class Meta:
        model = Reservas
        fields = '__all__'
        widgets = {
            'nome_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'CNPJ': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'quitado': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'stand': forms.Select(attrs={'class': 'form-control'}),
        }