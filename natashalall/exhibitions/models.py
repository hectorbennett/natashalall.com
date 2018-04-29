import os
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


def image_filename(instance, filename):
    """
    Used by the ArtworkImage class when uploading image to specify where they
    are stored and how they are named.
    """
    ext = filename.split('.')[-1]
    title = instance.get_title()
    filename = "{}.{}".format(title, ext)
    return os.path.join('exhibition', filename)


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


class ExhibitionImage(models.Model):
    exhibition = models.ForeignKey(
        Exhibition,
        related_name='images',
        on_delete=models.CASCADE
    )
    image_original = models.ImageField('exhibition', upload_to=image_filename)
    image_large = ImageSpecField(
        source='image_original',
        processors=[ResizeToFit(1500, 1500)],
        format='JPEG',
        options={'quality': 90}
    )
    image_medium = ImageSpecField(
        source='image_original',
        processors=[ResizeToFit(500, 500)],
        format='JPEG',
        options={'quality': 90}
    )
    image_small = ImageSpecField(
        source='image_original',
        processors=[ResizeToFit(150, 150)],
        format='JPEG',
        options={'quality': 90},
    )

    visible = models.BooleanField(default=True)

    def get_title(self):
        return self.exhibition.title
