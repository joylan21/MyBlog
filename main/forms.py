from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
from django import forms 
from django.contrib.auth.forms import UserCreationForm

from .models import Post

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','description','photo']