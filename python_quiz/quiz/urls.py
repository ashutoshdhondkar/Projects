from django.urls import path
from . import views
urlpatterns = [
	path('login/',views.index,name='index'),
	path('',views.Register,name='register'),
	path('Home/',views.Login,name='check'),
]