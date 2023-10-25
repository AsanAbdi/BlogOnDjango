from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['title', 'body', 'category', 'photo']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

class UpdatePostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['title', 'body', 'category', 'photo']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }