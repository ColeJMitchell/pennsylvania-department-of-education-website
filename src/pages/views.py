from django.http import HttpResponse
from django.shortcuts import render
from .models import entries

# Create your views here.
def home_page(request, *args, **kwargs):
    data = entries.objects.all()
    context = {entries:data}
    return render(request, "home.html", context)
