from django.contrib import admin
from django.db import models

from main.forms import AdminImageWidget

from .models import Exhibition
from .models import ExhibitionImage


class ExhibitionImageInline(admin.TabularInline):
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}

    model = ExhibitionImage
    extra = 1


class ExhibitionAdmin(admin.ModelAdmin):
    inlines = (ExhibitionImageInline, )
    filter_horizontal = ('artworks', )

    fieldsets = (
        (None, {
            'fields': (
                'title',
                'location',
                ('date', 'end_date'),
                'description',
                'url'
            )
        }),
        ('Artworks', {
            'fields': (
                'artworks',
            )
        }),
    )


admin.site.register(Exhibition, ExhibitionAdmin)
