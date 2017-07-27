from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^detail/$', views.post_create, name="detail"),
    url(r'^list/$', views.post_list, name="list"),
]