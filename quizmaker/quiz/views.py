from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register_Users,Questions,Marks
from django.http import JsonResponse
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


# def home(request):
# 	obj = Questions.objects.all()
# 	answers = []
# 	for x in obj:
# 		answers.append(x.ans_key)
# 	print(answers)

# 	context = {'data':obj,'answers':answers,'strength':len(answers)}
# 	return render(request,'quiz/home.html',context)
def Registration(request):
	if(request.method == 'POST'):

		username = request.POST['regusername']
		email = request.POST['regemail']
		phone = request.POST['regphone']
		password = request.POST['regpassword']
		# create object of user to be added
		obj = Register_Users(
				username = username,
				email = email,
				phone = phone,
				password = password
			)
		if(len(username)>1 and len(password)>1 and len(email)>1 and len(phone) >1):
			data = {
				'is_success' : True,
			}
			# add it to database	
			obj.save()
		else:
			data = {
				'is_success':False
			}
		
	return JsonResponse(data)

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

def validate_username(request):
	username = request.POST['username']
	print(username)
	data = {
		'is_taken' : Register_Users.objects.filter(username__exact = username).exists()

	}
	return JsonResponse(data)