from django.contrib import admin

from .models import Artwork
from .models import ArtworkImage
from .models import ArtworkVideo


class ArtworkImageInline(admin.TabularInline):
    model = ArtworkImage
    extra = 1


class ArtworkVideoInline(admin.TabularInline):
    model = ArtworkVideo
    extra = 1


class ArtworkAdmin(admin.ModelAdmin):
    inlines = (ArtworkImageInline, ArtworkVideoInline)
    filter_horizontal = ('exhibitions', )


admin.site.register(Artwork, ArtworkAdmin)
