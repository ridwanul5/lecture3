from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=4)
    # priority : another variable for forms 
# Create your views here.
tasks_py = ["foo", "boo", "baz"]

def index(request): 
    return render(request, "tasks/index.html", {
        "tasks_html": tasks_py
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks_py.append(task) #task_py e add hobe (not tasks_html)

        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })