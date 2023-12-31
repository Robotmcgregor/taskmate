from django.db import models
from django import forms
# from .models import Profile
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    profile_image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed

class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(label='Profile Picture', required=False)
    
    class Meta:
        model = Profile
        #fields = ['profile_image', ]
        fields = ('profile_image', )
    
