from django.shortcuts import render, redirect
from django.http import HttpResponse

def todolist(request):
    #return HttpResponse("Welcome")
    context = {
        'welcome_text':'Welcome To Todo List App!',
               }
    return render(request, 'todolist.html', context)
