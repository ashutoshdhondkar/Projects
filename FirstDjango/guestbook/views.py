from django.shortcuts import render,redirect
from .models import Comment
# Create your views here.
def index(request):
	comments = Comment.objects.order_by('-date_added')
	context = {'comments':comments}
	return render(request,'guestbook/index.html',context)

def sign(request):
	context = {}
	try:
		new_comment = Comment(name = request.POST.get('name'), comments = request.POST.get('comment'))
		if(new_comment.name and new_comment.comments):
			new_comment.save()
			data = "Thanks"
		else:
			data = "please"
	except Exception as e:
		print(e)
	if(data == 'please'):	
		context = {'data':data}
		return render(request,'guestbook/sign.html')
	else:
		return redirect('index')