from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index0(request):
    return HttpResponse("Hello, Hasan!")

def greet0(request, name):
    return HttpResponse(f"Hello, {name}!") # f = formatted string
    #{name} --> plugin the name


def greet(request, name):
    return render(request, "hello/greet.html", {
        "name5": name.capitalize()
    })


def index(request):
    return render(request, 'hello/index.html')