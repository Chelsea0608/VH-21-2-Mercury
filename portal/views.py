from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from portal.EmailBackend import EmailBackEnd
from django.contrib import messages
from portal.models import CustomUser
from django.urls import reverse
# Create your views here.


def showDemoPage(request):
    return render(request, "demo.html")


def ShowLoginPage(request):
    return render(request, "opt.html")

def redirstaff(request):
    return render(request, "login.html")

def redirstud(request):
    return render(request, "log.html")

def resignup(request):
    return render(request, "signup.html")

def doLogin(request):

    if request.method != "POST":
        return HttpResponse("<h2>Method not Allowed<h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get(
            "email"), password=request.POST.get("password"))
        if user != None:
            login(request, user)
            return HttpResponseRedirect("/staff_home")
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/")

def stuLogin(request):
    
    if request.method != "POST":
        return HttpResponse("<h2>Method not Allowed<h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get(
            "email"), password=request.POST.get("password"))
        if user != None:
            login(request, user)
            return HttpResponseRedirect("/student_home")
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")


def signup(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        stream = request.POST.get("stream")
        university = request.POST.get("university")
        try:
            user = CustomUser.objects.create_user(
                username=username, password=password, email=email, last_name=last_name, first_name=first_name, user_type=2)
            user.students.gender = gender
            user.students.stream = stream
            user.students.university = university
            user.save()
            login(request, user)
            subject = 'Welcome to E-Learning Portal'
            message = f'Hi {user.first_name}, thank you for registering in e-learning portal.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, "Successfully Registered! Mail Sent")
            return HttpResponseRedirect(reverse("resignup"))
        except:
            messages.error(request, "Try again")
            return HttpResponseRedirect(reverse("resignup"))
