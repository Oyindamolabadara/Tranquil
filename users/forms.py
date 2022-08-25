"""Users Registration Form"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """Users Creation Form"""
    email = forms.EmailField()

    class Meta:
        """Users Creation Form Model"""
        model = User
        fields = ['username', 'email', 'password1', 'password2']
