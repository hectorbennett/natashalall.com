from django.contrib import admin

from .models import PageContent
from .models import Artwork
from .models import ArtworkImage

# from .models import Shows


# admin.site.register(Artwork)
# admin.site.register(Shows)


# admin.py
class ArtworkImageInline(admin.TabularInline):
    model = ArtworkImage
    extra = 1

class ArtworkAdmin(admin.ModelAdmin):
    inlines = [ArtworkImageInline,]

admin.site.register(PageContent)
admin.site.register(Artwork, ArtworkAdmin)
