from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm #, ProfilePicForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# ----- new stuff -----
from django.contrib.auth import login, authenticate, logout


# def login_user(request):
#     if request.method == "POST":
        
#         #return render(request, 'contact.html')
#         username = request.POST['username']
#         password = request.POST['password']
        
#         # Check if user is in database
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             messages.success(request, ("You are now logged in!"))
#             return redirect('profile')
#         else:
#             messages.success(request, ("Error logging in, please try again!"))
#             return redirect('register')
#     else:
#         return render(request, 'contact.html')

# def register_user(request):
#     if request.method == "POST":
#         register_form = CustomUserCreationForm(request.POST)
#         if register_form.is_valid():
#             register_form.save()
#             username = form.cleaned_data.get['username']
#             password = form.cleaned_data.get['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request, ("New User Account Created, You Are Now Logged In!"))
            
#             return redirect('index')            
#     else:
#         register_form = CustomUserCreationForm()

#     return render(request, 'register.html', {'register_form':register_form})


# -------------------------- old stuff

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



