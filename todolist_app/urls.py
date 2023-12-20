from django.urls import path
from todolist_app import views


urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.about, name='about'),
    # path('task/delete/<task_id>', views.delete_task, name='delete_task'),
    # path('task/edit/<task_id>', views.edit_task, name='edit_task'),
    # path('task/complete/<task_id>', views.complete_task, name='complete_task'),
    # path('task/pending/<task_id>', views.pending_task, name='pending_task'),

]