import re

from django import template
from main.models import SocialMediaLink

register = template.Library()


@register.inclusion_tag('main/footer.html')
def footer():
    social_media_links = SocialMediaLink.objects.all()
    return {'social_media_links': social_media_links}


@register.inclusion_tag('main/nav.html', takes_context=True)
def nav(context):
    return {'request': context['request']}


@register.inclusion_tag('main/page_heading.html')
def page_heading(text=None, image=None):
    return {'text': text, 'image': image}


@register.simple_tag
def active(request, pattern):

    

    if not pattern:
        return ''

    print('path: ' + request.path)
    print('pattern: ' + pattern)
    print('-'*80)

    if pattern.startswith(request.path):
        return 'active'

    return ''

    # print(re.search(pattern, request.path))

    # if not request.path:
    #     return ''

    # if re.search(pattern, request.path):
    #     return 'active'
    # return ''
