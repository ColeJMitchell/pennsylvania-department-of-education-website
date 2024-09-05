from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")

def login_page(*args, **kwargs):
    return HttpResponse("<h1>This is a login page</h1>")
