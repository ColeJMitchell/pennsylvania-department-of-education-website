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
        district_submit = request.POST.get('district_submit')
        year_submit = request.POST.get('year_submit')

        filters = {}
        if school_submit != "Select Schools":
            filters['school'] = school_submit
        if district_submit != "Select District":
            filters['district'] = district_submit
        if year_submit != "Select Years":
            filters['years'] = year_submit

        if filters:
            data = enrollment.objects.filter(**filters)
        else:
            data = None 

        context = {
            'enrollment': data,
            'school_submit': school_submit,
            'district_submit': district_submit,
            'year_submit': year_submit,
        }
        return render(request, "plot.html", context)
    else:
        return render(request, "plot.html", {})

    
    
def comparison_page(request):
    if request.method == "POST":
        return render(request, "comparison.html", {})
    else:
        return render(request, "comparison.html", {})