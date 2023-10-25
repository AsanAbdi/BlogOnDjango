from django import forms
from .models import User
from django.core.exceptions import ValidationError

class CreateUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['email', 'password', 'avatar', 'name']

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'})
        }

class UpdateUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['name', 'password', 'avatar']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'})
        }

class LoginUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['email', 'password']

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'})
        }
