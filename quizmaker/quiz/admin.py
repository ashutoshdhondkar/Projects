from django.contrib import admin
from .models import Register_Users,Questions,Marks
# Register your models here.
admin.site.register([Register_Users,Questions,Marks])