from django.shortcuts import render, redirect

# Create your views here.
def stories(request):
	return render(request, 'stories.html', {})
