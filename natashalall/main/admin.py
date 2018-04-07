from django.contrib import admin

from .models import PageContent
from .models import SocialMediaLink
from .models import SocialMediaType

admin.site.register(PageContent)
admin.site.register(SocialMediaType)
admin.site.register(SocialMediaLink)
