from django import forms
from todolist_app.models import TaskList

# model indicates which database you are connecting to
class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task', 'done']