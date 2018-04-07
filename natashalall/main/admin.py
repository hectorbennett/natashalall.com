from django.contrib import admin

from .models import SiteConfig
from .models import SocialMediaLink
from .models import SocialMediaType

admin.site.register(SiteConfig)
admin.site.register(SocialMediaType)
admin.site.register(SocialMediaLink)
