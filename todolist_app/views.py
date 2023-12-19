from django.shortcuts import render, redirect
from django.http import HttpResponse

def todolist(request):
    #return HttpResponse("Welcome")
    return render(request, 'todolist.html', {})
