from django import forms
from .models import Vuelo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#Formulario para productos
class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = '__all__'
        
#Formulario para los usuarios
class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
      