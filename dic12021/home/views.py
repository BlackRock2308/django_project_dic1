from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.


def home(request):
    
    context = {}
    return render(request, "home/index.html", context)


def registrationPage(request):

    return render(request, "home/registration.html")

def loginUser(request):
    return render(request, "home/loginuser.html")



def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            
            user = form.cleaned_data.get('username')
            message = messages.success(request, "Your account has been created successfully for " + user)
            
            return redirect('register')

    context = {"form" : form}
    return render(request, "home/register.html", context)
    

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password )

        if user is not None:
            login(request, user)
            return redirect('index')
    
    context = {}
    return render(request, "home/index.html", context)


def logoutUser(request):
    logout(request)
    return redirect('index')            


def contact(request):
    mapbox_access_token = 'pk.eyJ1IjoibWJheWVtYzIiLCJhIjoiY2txcWRhMXh5MWc4ODJvcHF6Z3dudzdvbyJ9.NYhwiv_iLjOux8bg9e99Wg'
    context = {'mapbox_access_token': mapbox_access_token}
    return render(request, "home/contact.html", context)

def about(request):
    context = {}
    return render(request, "home/about.html", context)




#username : mbayemc2
#password : gnilanesene