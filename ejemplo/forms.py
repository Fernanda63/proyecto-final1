from django import forms

from ejemplo.models import Familiar
from ejemplo.models import Amigo
from ejemplo.models import Cliente


class Buscar(forms.Form):
    nombre = forms.CharField(max_length=10,
                            widget=forms.TextInput(attrs={'placeholder': 'Busque algo...'}))


class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']



class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

class AmigosForm(forms.ModelForm):
  class Meta:
    model = Amigo
    fields = ['nombre', 'direccion', 'numero_pasaporte']



class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

class ClientesForm(forms.ModelForm):
  class Meta:
    model = Cliente
    fields = ['nombre', 'direccion']