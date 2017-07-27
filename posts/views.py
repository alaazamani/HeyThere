from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def post_detail(request):
	instance = Post.objects.get(id=1)
	context = {
	"title": "Detail",
	"instance": instance
	}
	return render(request, 'post_detail.html', context)


def post_create(request):
	instance = Post.objects.get(id=1)
	context = {
	"title": "Detail",
	"instance": instance
	}
	return render(request, 'post_detail.html', context)

def post_list(request):
    object_list = Post.objects.all()
    context = {
    "object_list": object_list,
    "title": "List",
    "user": request.user
    }
    return render(request, 'post_list.html', context)
