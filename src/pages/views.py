from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request, *args, **kwargs):
    return render(request, "home.html", {})

def login_page(request, *args, **kwargs):
    return render(request, "login.html", {})