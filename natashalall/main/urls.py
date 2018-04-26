from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^info/$', views.info, name='info'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^work/', include('work.urls'), name='work'),
    url(r'^shows/', include('exhibitions.urls')),
]
