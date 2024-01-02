from django.db import models
from django import forms
# from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    #bio = models.TextField(max_length=500, blank=True)
    #location = models.CharField(max_length=30, blank=True)
    #birth_date = models.DateField(null=True, blank=True)
    #date_modified = models.DateTimeField(User, auto_now=True)
    profile_image = models.ImageField(null=True,
                                      blank=True,
                                      default='default.jpg', 
                                      upload_to='profile_pics')

    def __str__(self):
        return self.user.username
        #return f'{self.user.username} Profile' #show how we want it to be displayed


# class ProfilePicForm(forms.ModelForm):
#     profile_image = forms.ImageField(label='Profile Picture', required=False)
    
#     class Meta:
#         model = Profile
#         #fields = ['profile_image', ]
#         fields = ('profile_image', )
    
