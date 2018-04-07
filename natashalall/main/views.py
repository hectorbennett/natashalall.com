from django.shortcuts import render
from django.utils import timezone
from .models import SiteConfig, SocialMediaLink
from work.models import Artwork

site_config = SiteConfig.objects.get(id=1)


def index(request):
    main_image = site_config.homepage_artwork.images.first().image_large.url
    context = {'main_image': main_image}
    return render(request, 'main/index.html', context)


def info(request):
    info_text = site_config.information
    return render(request, 'main/info.html', {'info_text': info_text})


def contact(request):
    contact_info = site_config.contact_details
    return render(request, 'main/contact.html', {'contact_info': contact_info})
