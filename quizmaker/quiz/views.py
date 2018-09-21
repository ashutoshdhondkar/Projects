from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register_Users,Questions,Marks

# Create your views here.
def index(request):
	return render(request,'quiz/index.html')


def trial(request):
	if(request.is_ajax()):
		# print(f"id = {obj.id}")
		print("Inside trial")
		obj = Marks(
			userid = request.POST['userid'],
			marks = request.POST['tot'],
			)
		obj.save()
		
	return HttpResponse("")


def home(request):
	obj = Questions.objects.all()
	answers = []
	for x in obj:
		answers.append(x.ans_key)
	print(answers)

	context = {'data':obj,'answers':answers,'strength':len(answers)}
	return render(request,'quiz/home.html',context)
def Registration(request):
	if(request.method == 'POST'):

		username = request.POST['regusername']
		objnew = Register_Users.objects.all();
		for x in objnew:
			if(x.username == username):
				break
		else:
			# create object of user to be added
			obj = Register_Users(
					username = request.POST['regusername'],
					email = request.POST['regemail'],
					phone = request.POST['regphone'],
					password = request.POST['regpassword']
				)
			if(obj):
				print(obj)
				# add it to database	
				obj.save()
		
	return HttpResponse()

def login(request):
	if(request.method == 'POST'):
		username = request.POST['username']
		password = request.POST['password']
		print(username,password)
		# check whether user is registered or not
		obj1 = Register_Users.objects.filter(
				username__exact = username,
				password__exact = password
			)
		if(obj1):
			obj = Questions.objects.all()
			answers = []
			for x in obj:
				answers.append(x.ans_key)
			# print(answers)

			context = {'data':obj,'answers':answers,'strength':len(answers),'userdata':obj1[0]}
			return render(request,'quiz/home.html',context)
		else:
			return redirect('index')
	return HttpResponse()

