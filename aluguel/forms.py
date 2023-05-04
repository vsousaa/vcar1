from django.forms import ModelForm
from .models import Car, Cliente, Aluguel

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class AluguelForm(ModelForm):
    
    class Meta:
        model = Aluguel
        fields = '__all__'