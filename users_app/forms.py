from django import forms
from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# original django form
# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(label='Email Address', required=True)
#     #birth_date = forms.DateField(label='Birth Date', required=True)
#     class Meta:
#         model = User
#         fields = ['username', 
#                   'email', 
#                   #'birth_date', 
#                   'password1', 
#                   'password2']
        
        
class CustomCreationForm(UserCreationForm):
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 
                  'email', 
                  #'birth_date', 
                  'password1', 
                  'password2']

class MyUserAdmin(UserAdmin):  
    add_form = CustomCreationForm   

admin.site.register(User,MyUserAdmin)