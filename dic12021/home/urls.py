from django.urls import path
from .views import * 


urlpatterns = [
    path("",home, name = "index"),
    path("register/", registerPage, name= "register"),
    path("registration/", registrationPage, name= "registration"),
    path("loginuser/", loginUser, name="loginuser"),
    path("login/", loginPage, name= "login"),
    path("logout/", logoutUser, name = 'logout'),
    path("contact/",contact, name="contact"),
    path("about/", about, name= "about"),


]