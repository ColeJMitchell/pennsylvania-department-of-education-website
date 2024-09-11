from django.shortcuts import render
from .models import entries

# Create your views here.
def home_page(request):
    data = entries.objects.all()
    context = {'entries':data}
    return render(request, "home.html", context)
