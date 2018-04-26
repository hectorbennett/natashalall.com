from django.db import models


class Exhibition(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(
        max_length=255,
        blank=True,
        default=''
    )
    date = models.DateField(null=True)
    end_date = models.DateField('until', null=True, blank=True)
    description = models.TextField(blank=True)
    url = models.CharField(
        max_length=255,
        help_text='e.g. to the gallery webpage for this exhibition.',
        blank=True,
        default=''
    )
    artworks = models.ManyToManyField(
        'work.Artwork',
        verbose_name='exhibited artworks',
        help_text=(
            'Artworks can also be added to exhibitions from the artwork edit '
            'screen.'
        ),
        blank=True
    )
    live = models.BooleanField(
        'is live',
        default=True,
        help_text=(
            'If this is unchecked then this exhibition will not appear '
            'anywhere on the site.'
        ),
    )

    def __str__(self):
        return self.title_location_year

    class Meta:
        ordering = ['-date', 'title']

    @property
    def title_location_year(self):
        "Returns title, location, year."
        fields = (
            str(self.title),
            str(self.location),
            str(self.date.year)
        )
        return ', '.join(x for x in fields if x)

    @property
    def title_location(self):
        "Returns title, location."
        fields = (
            str(self.title),
            str(self.location)
        )
        return ', '.join(x for x in fields if x)
