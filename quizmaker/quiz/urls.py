from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('registration/',views.Registration,name='register'),
	path('home/',views.login,name='login'),
	# path('home/',views.home,name='home'),
	path('test/',views.trial,name='trial'),
	path('validate/',views.validate_username,name='validate')
]