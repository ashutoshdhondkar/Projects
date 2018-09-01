from django.shortcuts import render,redirect
from .models import Comment
# Create your views here.
def index(request):
	comments = Comment.objects.order_by('-date_added')
	context = {'comments':comments}
	return render(request,'guestbook/index.html',context)

def sign(request):
	try:
		new_comment = Comment(name = request.POST.get('name'), comments = request.POST.get('comment'))
		new_comment.save()
	except Exception as e:
		print(e)
	else:
		return redirect('index')
	return render(request,'guestbook/sign.html')