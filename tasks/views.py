from django.shortcuts import render

# Create your views here.
tasks_py = ["foo", "boo", "baz"]

def index(request): 
    return render(request, "tasks/index.html", {
        "tasks_html": tasks_py
    })

def add(request): 
    return render(request, "tasks/add.html")