from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu usuario'}),
                               help_text="<small>Requerido. 150 caracteres o menos. Letras, dígitos y @ /. / + / - / _ solamente.</small>")
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingresa tu correo'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingresa tu Nombre'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingresa tu Apellido'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text="<small><ul><li>Su contraseña no puede ser muy similar a su otra información personal.</li>\
                                    <li>Su contraseña debe contener al menos 8 caracteres.</li>\
                                    <li>Su contraseña no puede ser una contraseña de uso común.</li>\
                                    <li>Tu contraseña no puede ser completamente numérica.</li></ul></small>")
    password2 = forms.CharField(label="Confirmación de Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text="<small>Ingrese la misma contraseña que antes, para verificación.</small>")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2', ]