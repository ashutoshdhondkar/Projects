from django.shortcuts import render,redirect
from .models import Questions,Registered_Users
import hashlib
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request,'quiz/loginpage.html')

def Register(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	password = hashlib.md5(password.encode()).hexdigest()
	email_id = request.POST.get('email')
	phone_no = request.POST.get('phoneno')
	if(username and password and email_id and (len(phone_no) == 0 or len(phone_no) == 10) ):

		obj = Registered_Users(username = username,password = password,
				email_id = email_id,phone_no = phone_no)
		try:
			names = Registered_Users.objects.all()
			for x in names:
				if(x.username == username):
					break
			else:
				obj.save()
		except Exception as e:
			print(e)

		return redirect('index')

# def checkLogin()
def Login(request):
	try:
		username = request.POST.get('loginusername')

		password = request.POST.get('loginpassword')
		password = hashlib.md5(password.encode()).hexdigest()
		print(username,password)

	except Exception as e:
		pass

	obj = Registered_Users.objects.filter(username__exact = username , password__exact = password)
	if(obj):
		login_id = obj[0].id
		print(login_id)
		questions = Questions.objects.all()
		context = {'questions':questions}
		
		return render(request,'quiz/home.html',context)
	
	else:
		# pass
		#print("invalid")
		return redirect('index')

		# return render(request,'quiz/home.html',context)
	return redirect('index')
	# return redirect('index')
