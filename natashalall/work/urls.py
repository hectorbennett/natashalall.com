from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<pk>\d+)/$', views.artwork_detail, name='artwork_detail'),
] 
