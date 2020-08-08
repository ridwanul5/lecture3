from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=4)
    # priority : another variable for forms 
# Create your views here.



def index(request):
    if "tasks_py" not in request.session:
        request.session["tasks_py"] = []
    return render(request, "tasks/index.html", {
        "tasks_html": request.session["tasks_py"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks_py"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    else:
        return render(request, "tasks/add.html", {
            "form": NewTaskForm()
        })