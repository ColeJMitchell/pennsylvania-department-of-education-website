from django.shortcuts import render
from django.conf import settings
from django.core.serializers import serialize
from django.core.cache import cache
from .models import district, districtFiscal, districtKeystone, School, enrollment, SchoolEnrollment
import itertools
import json

# Create your views here.
def home_page(request):
    if request.method == "POST":
        return render(request, "home.html", {})
    else:
        return render(request, "home.html", {})

def map_page(request):
    api_key = settings.MAP_API_KEY

    cache_key = 'schools_json'
    schools_json = cache.get(cache_key)

    if not schools_json:
        schools = School.objects.exclude(latitude__isnull=True).exclude(longitude__isnull=True)
        school_data = []

        for school in schools:
            try:
                district_name = district.objects.get(district_id=school.district_id).district_name
            except district.DoesNotExist:
                district_name = "Self"

            # try to get school enrollment data for the school in 2023
            try:
                enrollment_data = SchoolEnrollment.objects.get(school_id=school.school_id, year=2023).school_enrollment
            except enrollment.DoesNotExist:
                enrollment_data = None

            school_data.append({
                'name': school.name,
                'district_name': district_name,
                'enrollment_data': enrollment_data,
                'address_street': school.address_street,
                'address_city': school.address_city,
                'website': school.website,
                'telephone': school.telephone,
                'elementary': school.elementary,
                'middle': school.middle,
                'high': school.high,
                'latitude': school.latitude,
                'longitude': school.longitude
            })
        schools_json = json.dumps(school_data)
        cache.set(cache_key, schools_json, 60)
    return render(request, "map.html", {"api_key": api_key, "schools": schools_json})

#renders the plot page if a post request is made for the page it determines if the post data is correct and then paasses the relevant data from the database to the front end
def plot_page(request):
    if request.method == "POST":
        keystone_list = ["numbers_scored", "percent_advanced", "percent_proficient", "percent_basic", "percent_below_basic"]
        fiscal_list = ["federal_revenue", "local_revenue", "state_revenue", "total_expenditures", "total_revenue"]
        district_post = request.POST.get('query')
        attribute_post = request.POST.get('dropdown')
        #error handling
        if not district_post or not attribute_post:
            return render(request, "plot.html", {})

        district_post = district_post.upper()

        if attribute_post in keystone_list:
            rows= []
            rows.append([attribute_post])
            keystone_data = districtKeystone.objects.filter(district_id__district_name=district_post)
            for data in keystone_data:
                rows.append([data.year, getattr(data, attribute_post), data.group, data.subject])
            return render(request, "plot.html", {'chart_data': json.dumps(rows)})

        if attribute_post in fiscal_list:
            rows = []
            fiscal_data = districtFiscal.objects.filter(district_id__district_name=district_post)
            for data in fiscal_data:
                rows.append([data.year, getattr(data, attribute_post)])
            print(rows)
            return render(request, "plot.html", {'fiscal_data': json.dumps(rows)})

        return render(request, "plot.html", {})

    else:
        return render(request, "plot.html", {})

#code to compare two schools in the front-end based on context sent from the front end
def comparison_page(request):
    if request.method == "POST":
        context = {}
        return render(request, "comparison.html", context)
    else:
        return render(request, "comparison.html", {})