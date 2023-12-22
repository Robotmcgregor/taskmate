from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm

def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('todolist')
    
    else:
        all_tasks = TaskList.objects.all()
        return render(request, 'todolist.html', {'all_tasks': all_tasks})
    
    context = {
        'todolist_text':'Welcome To Todo List App!',
        'all_tasks': all_tasks,
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
