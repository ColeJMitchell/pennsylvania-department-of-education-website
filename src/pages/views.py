from django.shortcuts import render
from django.conf import settings

# Create your views here.
def home_page(request):
    if request.method == "POST":
        return render(request, "prototype.html", {})
    else:
        return render(request, "prototype.html", {})

def map_page(request):
    api_key = settings.MAP_API_KEY
    if request.method == "POST":
        return render(request, "map.html", {"api_key": api_key})
    
def plot_page(request):
    if request.method == "POST":
        return render(request, "plot.html", {})
    else:
        return render(request, "plot.html", {})
    
    
def comparison_page(request):
    if request.method == "POST":
        return render(request, "comparison.html", {})
    else:
        return render(request, "comparison.html", {})