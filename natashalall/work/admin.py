from django.contrib import admin
from django.db import models

from main.forms import AdminImageWidget

from .models import Artwork
from .models import ArtworkImage
from .models import ArtworkVideo
from .models import ArtworkAudio


class ArtworkImageInline(admin.TabularInline):
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}

    model = ArtworkImage
    extra = 1


class ArtworkVideoInline(admin.TabularInline):
    model = ArtworkVideo
    extra = 1


class ArtworkAudioInline(admin.TabularInline):
    model = ArtworkAudio
    extra = 1


class ArtworkAdmin(admin.ModelAdmin):
    inlines = (ArtworkImageInline, ArtworkVideoInline, ArtworkAudioInline)
    filter_horizontal = ('exhibitions', )

    fieldsets = (
        (None, {
            'fields': (
                'title',
                'date',
                'description',
                'live',
            )
        }),
        ('Exhibitions', {
            'fields': (
                'exhibitions',
            )
        }),
    )


admin.site.register(Artwork, ArtworkAdmin)
