from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser 


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        max_length=255,
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    full_name = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = CustomUser
        fields = ['username','email', 'password']
        
class SignInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})) 
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

