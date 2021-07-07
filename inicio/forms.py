from django import forms
from django.forms.fields import CharField
from .models import Articulo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormArticulo(forms.ModelForm):

    #campos del modelo
    class Meta:
        model = Articulo
        fields = ('seccion', 'fecha_publicacion', 'titulo', 'contenido', 'imagen','precio')
        widgets = {
            'fecha_publicacion': forms.SelectDateWidget(attrs={'class': 'pub_fecha_publicacion'}),
            'titulo': forms.TextInput(attrs={'class': 'pub_titulo'}),
            'contenido': forms.Textarea(attrs={'class': 'pub_contenido'}),
            'imagen': forms.FileInput(attrs={'name':'imagen_adjunta', 'class': 'pub_imagen'}),
            'precio':forms.TextInput(attrs={'class':'pub_precio'}),
        }

class UserRegisterform(UserCreationForm):
    email= forms.EmailField()
    password1 =CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 =CharField(label='Confirma contraseña', widget=forms.PasswordInput)
    
    class Meta:
         model = User
         fields = ['username','email', 'password1', 'password2']
         help_texts = {k:"" for k in fields}