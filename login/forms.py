from django import forms
from .models import User

class LoginForm(forms.Form):
    user_email = forms.EmailField(label='Email')
    user_password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
