from django.shortcuts import render
from django.utils import timezone
from .models import SiteConfig, SocialMediaLink
from work.models import Artwork


def index(request):
    try:
        main_image = (
            SiteConfig.load().homepage_artwork.images.first().image_large.url
        )
    except AttributeError:
        main_image = ''
    context = {'main_image': main_image}
    return render(request, 'main/index.html', context)


def info(request):
    info_text = SiteConfig.load().information
    return render(request, 'main/info.html', {'info_text': info_text})


def contact(request):
    contact_info = SiteConfig.load().contact_details
    return render(request, 'main/contact.html', {'contact_info': contact_info})
