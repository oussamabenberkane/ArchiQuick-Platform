from django.contrib import admin
from django.contrib.auth.models import User


ouss = User.objects.get(username="ouss")
ouss.is_staff = True
ouss.is_admin = True
ouss.is_superuser = True
ouss.save()

rahim = User.objects.get(username="rahim")
rahim.is_staff = True
rahim.is_admin = True
rahim.is_superuser = True
rahim.save()
