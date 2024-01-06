from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def stories(request):
	return render(request, 'stories.html', {})

# @login_required
# def profile_list(request):
#     profiles = Profile.objects.exclude(user=request.user)
#     return render(request, 'profile_list.html', {"profiles_view": profiles})
