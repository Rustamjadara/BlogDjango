from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect	
from django.shortcuts import render,get_object_or_404,redirect

from .models import Post
from .forms import PostForm
# Create your views here.

def post_create(request):
	form = PostForm(request.POST or None)
	# if request.method =="POST":
	# 	print request.POST.get("title")
	# 	print request.POST.get("content")
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Succesfully created.")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request,"Error!,Post Not created.")
	context = {
		"form": form,
	}
	return render(request,"post_form.html",context)

def post_detail(request,id):
	instance = get_object_or_404(Post,id=id)
	context = {
		"instance": instance,
		"title"   : instance.title
	}
	return render(request,"post_detail.html",context)
def post_list(request):
	queryset = Post.objects.all()
	context = {
		"object_list":queryset,
		"title": "List"
	}
	return render(request,"index.html",context)

def post_update(request,id):
	instance = get_object_or_404(Post,id=id)
	form = PostForm(request.POST or None,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Succesfully updated.")

		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request,"Error! Post Not Updated")

	context = {
		"instance": instance,
		"title"   : instance.title,
		"form"    : form,
	}
	return render(request,"post_form.html",context)

def post_delete(request,id):
	instance = get_object_or_404(Post,id=id)
	instance.delete()
	return redirect("posts:list") 

