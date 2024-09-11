from django.shortcuts import render
from .models import entries

# Create your views here.
def home_page(request):
    #Once a user pressed update a post request is made
    if request.method == 'POST':
        data = entries.objects.all()
        context = {'entries':data}
        first_entry = entries.objects.first() 
        first_entry.year += 1 
        first_entry.save()


    #First get request when user first enters our website
    data = entries.objects.all()
    context = {'entries':data}
    return render(request, "home.html", context)
