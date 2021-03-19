"""learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from portal import views, StaffViews
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from learn import settings

urlpatterns = [
    path('demo/', views.showDemoPage),
    path('admin/', admin.site.urls),
    path('', views.showDemoPage, name='login'),
    path('option', views.ShowLoginPage, name='log'),
    path('redirstaff', views.redirstaff, name='restf'),
    path('redirstud', views.redirstud, name='restud'),
    path('resignup', views.resignup, name='resignup'),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user, name='logout'),

    path('doLogin', views.doLogin),
    path('stuLogin', views.stuLogin),
    path('staff_home', StaffViews.staff_home, name='staff_home'),
    path('staff_home/profile', StaffViews.view_profile, name='prof'),
    path('student_home', StaffViews.stud_home),
    path('signup', views.signup, name='signup')
]
