from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MyUserCreate(UserCreationForm):
    email = forms.EmailField(max_length=254,help_text="Обязательное поле")
    
    class Meta:
       model = User
       fields = ('username','email','password1','password2',)