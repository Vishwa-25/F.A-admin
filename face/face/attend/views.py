from django.shortcuts import render
from django.http import HttpResponse
from .models import gender


# Create your views here.

def home(request):
    return render(request, "base.html")


def admin(request, Post=gender):
    context = {'Post': gender}
    return render(request, "admin.html", context)


def security(request):
    return render(request, "security.html")
