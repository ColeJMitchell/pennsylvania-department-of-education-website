from django.shortcuts import render
from django.conf import settings
from .models import district, districtFiscal, districtKeystone
import itertools

# Create your views here.
def home_page(request):
    if request.method == "POST":
        return render(request, "home.html", {})
    else:
        return render(request, "home.html", {})

def map_page(request):
    api_key = settings.MAP_API_KEY
    if request.method == "POST":
        return render(request, "map.html", {"api_key": api_key})

#renders the plot page if a post request is made for the page it determines if the post data is correct and then paasses the relevant data from the database to the front end
def plot_page(request):
    if request.method == "POST":
        keystone_list = ["numbers_scored", "percent_advanced", "percent_proficient", "percent_basic", "percent_below_basic"]
        fiscal_list = ["federal_revenue", "local_revenue", "state_revenue", "total_expenditures", "total_revenue"]
        district_post = request.POST.get('query')
        attribute_post = request.POST.get('dropdown')
        
        if not district_post or not attribute_post:
            return render(request, "plot.html", {})
        
        district_post = district_post.upper()
        
        if attribute_post in keystone_list:
            years = []
            values = []
            keystone_data = districtKeystone.objects.filter(district_id__district_name=district_post)
            for data in keystone_data:
                years.append(data.year)
                values.append(getattr(data, attribute_post))
            chart_data = {
            "years": years,
            "values": values
            }
            print(chart_data)
            return render(request, "plot.html", {'chart_data': chart_data})
        
        if attribute_post in fiscal_list:
            years = []
            values = []
            fiscal_data = districtFiscal.objects.filter(district_id__district_name=district_post)
            for data in fiscal_data:
                years.append(data.year)
                values.append(getattr(data, attribute_post))
            chart_data = {
            "years": years,
            "values": values
            }
            print(chart_data)
            return render(request, "plot.html", {'chart_data': chart_data})

        return render(request, "plot.html", {})
    
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

        if school_submit != "Select School":
            filters1['school'] = school_submit
        if district_submit != "Select District":
            filters1['district'] = district_submit
        if year_submit != "Select Years":
            filters1['years'] = year_submit

        # Filters for the second set of inputs
        filters2 = {}

        if school_submit2 != "Select School 2":
            filters2['school'] = school_submit2
        if district_submit2 != "Select District 2":
            filters2['district'] = district_submit2
        if year_submit2 != "Select Years 2":
            filters2['years'] = year_submit2

        # Query db for data or set to empty list if filters are empty
        data1 = enrollment.objects.filter(**filters1) if filters1 else []
        data2 = enrollment.objects.filter(**filters2) if filters2 else []

        # Combine data1 and data2 using zip_longest
        combined_enrollment = itertools.zip_longest(data1, data2, fillvalue=None)

        # Create context
        context = {
            'combined_enrollment': combined_enrollment,
            'school_submit': school_submit,
            'district_submit': district_submit,
            'year_submit': year_submit,
            'school_submit2': school_submit2,
            'district_submit2': district_submit2,
            'year_submit2': year_submit2,
        }
        return render(request, "comparison.html", context)
    else:
        return render(request, "comparison.html", {})
