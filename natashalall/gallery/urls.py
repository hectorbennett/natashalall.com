from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^work/$', views.work, name='work'),
]