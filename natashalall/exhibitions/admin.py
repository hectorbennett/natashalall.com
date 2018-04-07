from django.contrib import admin

from .models import Exhibition


class ExhibitionAdmin(admin.ModelAdmin):
    filter_horizontal = ('artworks', )


admin.site.register(Exhibition, ExhibitionAdmin)
