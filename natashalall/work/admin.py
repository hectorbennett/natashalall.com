from django.contrib import admin

from .models import Artwork
from .models import ArtworkImage


class ArtworkImageInline(admin.TabularInline):
    model = ArtworkImage
    extra = 1


class ArtworkAdmin(admin.ModelAdmin):
    inlines = [ArtworkImageInline, ]

admin.site.register(Artwork, ArtworkAdmin)
