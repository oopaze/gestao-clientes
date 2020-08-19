from django.forms import ModelForm
from .models import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'cidade', 'estado', 'nascimento', 'foto']
