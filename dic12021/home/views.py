from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, "home/index.html", context)

def contact(request):
    context = {}
    return render(request, "home/contact.html", context)

def about(request):
    context = {}
    return render(request, "home/about.html", context)




#username : mbayemc2
#password : gnilanesene