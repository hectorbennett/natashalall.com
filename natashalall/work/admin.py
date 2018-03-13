from django.contrib import admin

from .models import Artwork
from .models import ArtworkImage
from .models import ArtworkVideo
from .models import Exhibition


class ArtworkImageInline(admin.TabularInline):
    model = ArtworkImage
    extra = 1


class ArtworkVideoInline(admin.TabularInline):
    model = ArtworkVideo
    extra = 1


class ArtworkAdmin(admin.ModelAdmin):
    inlines = [ArtworkImageInline, ArtworkVideoInline, ]


admin.site.register(Artwork, ArtworkAdmin)

admin.site.register(Exhibition)
