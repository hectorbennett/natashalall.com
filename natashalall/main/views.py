from django.shortcuts import render
from django.utils import timezone
from .models import PageContent
from .models import Shows


def index(request):
    page_content = PageContent.objects.filter(name='home_text').first()
    return render(request, 'main/index.html', {'page_content': page_content})


def info(request):
    info_text = PageContent.objects.filter(name='info_text').first()
    return render(request, 'main/info.html', {'info_text': info_text})


def shows(request):
    shows = Shows.object.order_by('start_date')
    return render(request, 'main/shows.html', {'shows': shows})


def contact(request):
    contact_info = PageContent.objects.filter(name='contact_info').first()
    return render(request, 'main/contact.html', {'contact_info': contact_info})
