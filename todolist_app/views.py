from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            # save(commit=False) is used to tell django not to save the form yet
            instance = form.save(commit=False)
            # we are setting the manage field to the current user
            instance.manage = request.user
            form.save()
        messages.success(request, ("New Task Added!"))
        
        return redirect('todolist')
    
    else:
        all_tasks = TaskList.objects.all()
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)

        return render(request, 'todolist.html', {'all_tasks': all_tasks})

@login_required    
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    
    return redirect('todolist')

@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()
    
    return redirect('todolist')

@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    
    return redirect('todolist')

@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        # instance is used to tell django which object to update
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()       
        messages.success(request, ("Task Edited!"))
        
        return redirect('todolist')
    
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        
        return render(request, 'edit.html', {'task_obj': task_obj})


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


def index(request):
    #return HttpResponse("Welcome To The Task Page.")
    context = {
        'index_text': 'Welcome to index page.',
    }
    return render(request, 'index.html', context)
