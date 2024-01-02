from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm #, ProfilePicForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

# ----- new stuff -----
#from django.contrib.auth import login, authenticate, logout

#working code
def register_user(request):
    if request.method == "POST":
        register_form = CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New User Account Created, Login To Get Started!"))
            
            return redirect('login')            
    else:
        register_form = CustomUserCreationForm()

    return render(request, 'register.html', {'register_form':register_form})


@login_required # Require user logged in before they can access profile page
def profile(request):
    return render(request, 'profile.html')


@login_required # Require user logged in before they can access profile page
def edit_profile(request):
    return render(request, 'edit_profile.html')


