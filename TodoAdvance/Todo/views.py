from django.shortcuts import render,redirect
from .models import TodoDB
from .forms import TodoForm
from django.http import HttpResponse
# Create your views here.

def index(request):
    form = TodoForm(request.POST)
    data = TodoDB.objects.all()
    context = {'form':form,'data':data}
    return render(request,'index.html',context)

def addTask(request):
    form = TodoForm(request.POST)
    if(form.is_valid()):
        data = TodoDB(task = request.POST['task'])
        data.save()
    return redirect('index')

def completed(request,task_id):
    data = TodoDB.objects.get(pk=task_id)
    data.complete = True;
    data.save()
    return redirect('index')

def delete(request):
    data = TodoDB.objects.filter(complete__exact=True)
    data.delete()
    return redirect('index')

def deleteall(request):
    TodoDB.objects.all().delete()
    return redirect('index')
    