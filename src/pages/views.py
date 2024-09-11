from django.shortcuts import render
from .models import entries

# Create your views here.
def home_page(request):
    #Once a user pressed update a post request is made
    if request.method == 'POST':
        if 'update' in request.POST:
            first_entry = entries.objects.first() 
            first_entry.year += 1 
            first_entry.save()
        elif 'write' in request.POST:
            new_entry = entries(year = 2017, aun = 112358132, county = "Washington", name = "Cheston")
            new_entry.save()


    #First get request when user first enters our website
    data = entries.objects.all()
    context = {'entries':data}
    return render(request, "home.html", context)
