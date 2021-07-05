from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, "home/index.html", context)

def contact(request):
    mapbox_access_token = 'pk.eyJ1IjoibWJheWVtYzIiLCJhIjoiY2txcWRhMXh5MWc4ODJvcHF6Z3dudzdvbyJ9.NYhwiv_iLjOux8bg9e99Wg'
    context = {'mapbox_access_token': mapbox_access_token}
    return render(request, "home/contact.html", context)

def about(request):
    context = {}
    return render(request, "home/about.html", context)




#username : mbayemc2
#password : gnilanesene