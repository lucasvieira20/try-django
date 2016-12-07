from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from .models import Post

def posts_create(request): 
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	# if request.method =="POST":
	# 	print request.POST.get("title")
	# 	print request.POST.get("content")
	# 	Post.objects.create(title=title)

	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)


def posts_detail(request, id=None):  #retrieve
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.title,
		"instance": instance
	}

	return render(request, "post_detail.html", context)



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

