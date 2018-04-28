from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=100)