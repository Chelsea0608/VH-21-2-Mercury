from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db import connection
from .models import Staffs
import base64

def staff_home(request):
    current_user = request.user
    return render(request, 'admin_template/base_template.html', {'user': current_user})

def stud_home(request):
    current_user = request.user
    return render(request, 'admin_template/stud_template.html', {'user': current_user})

def view_profile(request):
    current_user = request.user
    if current_user.is_authenticated:
        return render(request, 'admin_template/prof.html', {'user': current_user})

