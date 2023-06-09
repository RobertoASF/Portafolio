from .models import Affinity, UserScore
from django import forms
from .models import Comment, User


class LoginForm(forms.Form):
    user_email = forms.EmailField(label='Email')
    user_password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

class RegistrationForm(forms.Form):
    user_id = forms.CharField(label='Rut', max_length=255)
    user_name1 = forms.CharField(label='Nombre', max_length=255)
    user_name2 = forms.CharField(label='Segundo nombre', max_length=255, required=False)
    user_surname1 = forms.CharField(label='Apellido', max_length=255)
    user_surname2 = forms.CharField(label='Segundo apellido', max_length=255, required=False)
    user_email = forms.EmailField(label='Correo electrónico', max_length=255)
    user_password = forms.CharField(label='Contraseña', max_length=255, widget=forms.PasswordInput)
    user_phone = forms.IntegerField(label='Teléfono')
    user_inetrest1 = forms.ModelChoiceField(
        label='Interés 1',
        queryset=Affinity.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    user_interest2 = forms.ModelChoiceField(
        label='Interés 2',
        queryset=Affinity.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    user_photo = forms.ImageField(label='Foto', required=False)

class AdminForm(forms.Form):
    admin_email = forms.CharField(max_length=255)
    admin_name1 = forms.CharField(max_length=255)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class UserScoreForm(forms.ModelForm):
    class Meta:
        model = UserScore
        fields = ['user_reviwed', 'score_value']
