from django.contrib import admin

from .models import Exhibition


class ExhibitionAdmin(admin.ModelAdmin):
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
