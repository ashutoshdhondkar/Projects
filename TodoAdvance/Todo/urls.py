from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index,name='index'),
    path('add/',views.addTask,name='add'),
    path('complete/<task_id>',views.completed,name='complete'),
    path('deleteco/',views.delete,name='deleteco'),
    path('delly/',views.deleteall,name='ashutosh'),
] 