from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Post

def posts_create(request): 
	return HttpResponse("<h1>Create</h1>")

def posts_detail(request):  #retrieve
	context = {
		"title": "Detail"
	}
	return render(request, "index.html", context)

def posts_list(request): #list itens
	
	queryset = Post.objects.all()

	context = {
	 	"object_list": queryset,
		"title": "List",
	}

	# user_auth = request.user.is_authenticated()
	# if user_auth:
	# 	context = {
	# 		"title": "My User List"
	# 	}
	# else:

	return render(request, "index.html",context)

def posts_update(request): 
	return HttpResponse("<h1>Update</h1>")

def posts_delete(request): 
	return HttpResponse("<h1>Delete</h1>")

