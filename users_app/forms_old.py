
from django import forms
#from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

#original django form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email Address', required=True, widget=forms.EmailInput(attrs={'class':'form-control'}) )
    first_name = forms.CharField(label='First Name', max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form-control'}) )   
    last_name = forms.CharField(label='Last Name', max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form-control'}) ) 
    #birth_date = forms.DateField(label='Birth Date', required=True)
    class Meta:
        model = User
        fields = [
                  'first_name',
                  'last_name',
                  'username', 
                  'email', 
                  #'birth_date', 
                  'password1', 
                  'password2']
        
  
      
