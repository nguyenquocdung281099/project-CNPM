from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
class getFormLogin(forms.Form):
    username= forms.CharField(label="username", max_length=50)
    password=forms.CharField(label="password", max_length=50)
    