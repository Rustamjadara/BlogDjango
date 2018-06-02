from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse,HttpResponseRedirect	
from django.shortcuts import render,get_object_or_404,redirect

from .models import Post
from .forms import PostForm
# Create your views here.

def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	# if request.method =="POST":
	# 	print request.POST.get("title")
	# 	print request.POST.get("content")
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Succesfully created.")
		return HttpResponseRedirect(instance.get_absolute_url())
	#else:
		#messages.error(request,"Error!,Post Not created.")
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
	queryset = Post.objects.all().order_by("-timestamp")
	paginator = Paginator(queryset, 4) # Show 10 object_list per page
	page_req_var = "page"
	page = request.GET.get(page_req_var)
	try:
	 	object_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		object_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		object_list = paginator.page(paginator.num_pages)

	context = {
		"object_list":queryset,
		"title": "List",
		"object_list":object_list,
		"page_req_var":page_req_var

	}
	return render(request,"post_list.html",context)

def post_update(request,id):
	instance = get_object_or_404(Post,id=id)
	form = PostForm(request.POST or None, request.FILES or None,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Succesfully updated.")

		return HttpResponseRedirect(instance.get_absolute_url())
	#else:
		#messages.error(request,"Error! Post Not Updated")

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

