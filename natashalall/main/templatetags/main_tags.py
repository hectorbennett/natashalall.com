from django import template
from main.models import SocialMediaLink

register = template.Library()


@register.inclusion_tag('main/footer.html')
def footer():
    social_media_links = SocialMediaLink.objects.all()
    return {'social_media_links': social_media_links}


@register.inclusion_tag('main/nav.html')
def nav():
    return {}


@register.inclusion_tag('main/page_heading.html')
def page_heading(text=None, image=None):
    return {'text': text, 'image': image}
