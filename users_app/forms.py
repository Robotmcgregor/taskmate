from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email Address', required=True)
    #birth_date = forms.DateField(label='Birth Date', required=True)
    class Meta:
        model = User
        fields = ['username', 
                  'email', 
                  #'birth_date', 
                  'password1', 
                  'password2']