from django.contrib import admin
from .models import Questions,Registered_Users
# Register your models here.

admin.site.register([Questions,Registered_Users])