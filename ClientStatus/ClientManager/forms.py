from django import forms
from django.contrib.auth.forms import AuthenticationForm

from ClientManager.models import Client


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'login-form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'pass-form-control'}))


class ClientStatusForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['status']
