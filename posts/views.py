from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Post
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote
from .forms import PostForm

def post_home(request):
    return HttpResponse("<h1> Hello</h1>")


def post_detail(request, post_id):
	instance = get_object_or_404(Post, id=post_id)
	context = {
	"title": "Detail",
	"instance": instance
	}
	return render(request, 'post_detail.html', context)


def post_create(request):
    form = PostForm(request.POST or None)
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
	object_list = Post.objects.all().order_by("-timestamp","-updated")
	context = {
	"object_list": object_list,
	"title": "List",
	"user": request.user
	}
	return render(request, 'post_list.html', context)

def post_update(request, post_id):
    instance = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance = instance)
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

def post_delete(request, post_id):
    instance = get_object_or_404(Post, id=post_id)
    instance.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("posts:list")
