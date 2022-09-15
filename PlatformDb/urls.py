"""PlatformDb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
#   in django: views = actions (functions)
#   authentication related views
from authentication.views import signupaction, contactaction, loginaction, logoutaction
#   main platform related views
from main.views import homeaction, profileaction
#   forum related views
from stack.views import main_stackaction

urlpatterns = [
    path("admin/", admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path("contact/signup/", signupaction, name='signup'),
    path("contact/login/", loginaction, name='login'),
    path("logout/", logoutaction, name='logout'),
    path("contact/", contactaction, name='contact'),
    path("profile/", profileaction, name='profile'),
    path("stack/", main_stackaction, name='stack' ),
    path("", homeaction, name='home')

    #   name='': for accessing url without writing the whole reference
]
