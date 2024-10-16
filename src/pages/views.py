from django.shortcuts import render
from django.conf import settings
from .models import enrollment

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
        school_submit = request.POST.get('school_submit')
        county_submit = request.POST.get('county_submit')
        year_submit = request.POST.get('year_submit')
        data = enrollment.objects.filter(school=school_submit, district=county_submit, years=year_submit)
        print(school_submit, county_submit, year_submit)
        context = {
            'enrollment': data
        }
        return render(request, "plot.html", context)

    else:
        return render(request, "plot.html", {})
    
    
def comparison_page(request):
    if request.method == "POST":
        return render(request, "comparison.html", {})
    else:
        return render(request, "comparison.html", {})