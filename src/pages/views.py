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
        if district_submit != "Select Districts":
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
        print("Filters:", filters)
        print("Data:", data)
        return render(request, "plot.html", context)
    else:
        return render(request, "plot.html", {})


def comparison_page(request):
    if request.method == "POST":
        # Retrieve values for the first set of inputs
        school_submit = request.POST.get('school_submit')
        district_submit = request.POST.get('district_submit')
        year_submit = request.POST.get('year_submit')

        # Retrieve values for the second set of inputs
        school_submit2 = request.POST.get('school_submit2')
        district_submit2 = request.POST.get('district_submit2')
        year_submit2 = request.POST.get('year_submit2')

        # Filters for the first set of inputs
        filters1 = {}

        if school_submit != "Select Schools":
            filters1['school'] = school_submit
        if district_submit != "Select Districts":
            filters1['district'] = district_submit
        if year_submit != "Select Years":
            filters1['years'] = year_submit

        # filters for the second set of inputs
        filters2 = {}

        if school_submit2 != "Select Schools 2":
            filters2['school'] = school_submit2
        if district_submit2 != "Select Districts 2":
            filters2['district'] = district_submit2
        if year_submit2 != "Select Years 2":
            filters2['years'] = year_submit2

        # Query db for data
        data1 = enrollment.objects.filter(**filters1) if filters1 else None
        data2 = enrollment.objects.filter(**filters2) if filters2 else None

        # Create context
        context = {
            'enrollment1': data1,
            'school_submit1': school_submit,
            'district_submit1': district_submit,
            'year_submit1': year_submit,
            'enrollment2': data2,
            'school_submit2': school_submit2,
            'district_submit2': district_submit2,
            'year_submit2': year_submit2,
        }
        return render(request, "comparison.html", context)
    else:
        return render(request, "comparison.html", {})