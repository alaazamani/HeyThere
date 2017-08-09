from django.conf.urls import url
from api.views import *


urlpatterns = [
	url(r'^list/$', PostListAPIView.as_view(), name="list"),
]