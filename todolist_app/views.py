from django.shortcuts import render, redirect
from django.http import HttpResponse

def todolist(request):
    #return HttpResponse("Welcome")
    context = {
        'todolist_text':'Welcome To Todo List App!',
               }
    return render(request, 'todolist.html', context)

def contact(request):
    #return HttpResponse("Welcome")
    context = {
        'contact_text':'Welcome To Contact Us!',
               }
    return render(request, 'contact.html', context)

def about(request):
    #return HttpResponse("Welcome")
    context = {
        'about_text':'Welcome To About Us!',
               }
    return render(request, 'about.html', context)
