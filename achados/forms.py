from django import forms
from .models import Objeto, Sala

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ["nome", "descricao"]


class ObjetoForm(forms.ModelForm):
    class Meta:
        model = Objeto
        fields = ["nome", "descricao", "local_encontrado"]
