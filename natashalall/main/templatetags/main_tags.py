import re

from django import template
from main.models import SocialMediaLink
from main.models import SiteConfig

register = template.Library()


@register.inclusion_tag('main/footer.html')
def footer():
    social_media_links = SocialMediaLink.objects.all()
    copyright_line = SiteConfig.load().copyright_line
    context = {
        'social_media_links': social_media_links,
        'copyright_line': copyright_line
    }
    return context


@register.inclusion_tag('main/nav.html', takes_context=True)
def nav(context):
    return {'request': context['request']}


@register.inclusion_tag('main/page_heading.html')
def page_heading(text=None, image=None):
    return {'text': text, 'image': image}
