from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from .models import Post
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote
from .forms import PostForm

def post_home(request):
	return HttpResponse("<h1> Hello</h1>")


def post_detail(request, post_slug):
	instance = get_object_or_404(Post, slug=post_slug)
	context = {
	"title": "Detail",
	"instance": instance,
	"share_string": quote(instance.content)
	}
	return render(request, 'post_detail.html', context)


def post_create(request):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Successfully Created!")
		return redirect("posts:list")
	context = {
	"title": "Create",
	"form": form,
	}
	return render(request, 'post_create.html', context)

def post_list(request):
	object_list = Post.objects.all() #.order_by("-timestamp","-updated")

	paginator = Paginator(object_list, 5) # Show 5 contacts per page
	page = request.GET.get('page')
	try:
		objects = paginator.page(page)
	except PageNotAnInteger:
		objects = paginator.page(1)
	except EmptyPage:
		objects = paginator.page(paginator.num_pages)
	context = {
	"object_list": objects,
	"title": "List",
	"user": request.user
	}
	return render(request, 'post_list.html', context)

def post_update(request, post_slug):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
	instance = get_object_or_404(Post, slug=post_slug)
	form = PostForm(request.POST or None,  request.FILES or None, instance = instance)
	if form.is_valid():
		form.save()
		messages.success(request, "Successfully Edited!")
		return redirect(instance.get_absolute_url())
	context = {
	"form":form,
	"instance": instance,
	"title": "Update",
	}
	return render(request, 'post_update.html', context)

def post_delete(request, post_slug):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
	instance = get_object_or_404(Post, slug=post_slug)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	return redirect("posts:list")
