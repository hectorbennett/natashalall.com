from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^work/$', views.work, name='work'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)