from django import template
from main.models import SocialMediaLink

register = template.Library()


@register.inclusion_tag('work/artwork_grid.html')
def artwork_grid(artworks):
    return {'artworks': artworks}
