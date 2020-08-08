from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)
    # priority : another variable for forms 
# Create your views here.
tasks_py = ["foo", "boo", "baz"]

def index(request): 
    return render(request, "tasks/index.html", {
        "tasks_html": tasks_py
    })

def add(request): 
    return render(request, "tasks/add.html", {
            "form": NewTaskForm()
    })