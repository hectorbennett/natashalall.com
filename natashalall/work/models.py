import os
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

from exhibitions.models import Exhibition


def image_filename(instance, filename):
    """
    Used by the ArtworkImage class when uploading image to specify where they
    are stored and how they are named.
    """
    ext = filename.split('.')[-1]
    title = instance.get_title()
    filename = "%s.%s" % (title, ext)
    return os.path.join('artwork', filename)


class Artwork(models.Model):
    title = models.CharField(max_length=100)
    creation_date = models.DateField(
        help_text="You can just put 01/01/xxxx if you only know the year"
    )
    description = models.TextField(blank=True, null=True)
    exhibitions = models.ManyToManyField(
        Exhibition,
        through=Exhibition.artworks.through,
        verbose_name='exhibited in',
        help_text="""
            Artworks can also be added to exhibitions from the exhibition edit
            screen.
        """,
        blank=True,
    )

    class Meta:
        ordering = ['creation_date', 'title']

    def _get_title_and_year(self):
        "Returns the title and year."
        return ', '.join((str(self.title), str(self.creation_date.year)))

    title_and_year = property(_get_title_and_year)

    def __str__(self):
        return self.title_and_year


class ArtworkImage(models.Model):
    artwork = models.ForeignKey(Artwork, related_name='images')
    image_original = models.ImageField(upload_to=image_filename)
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

    visible = models.BooleanField(default=True)

    def get_title(self):
        return self.artwork.title


class ArtworkVideo(models.Model):
    artwork = models.ForeignKey(Artwork, related_name='videos')
    url = models.CharField(
        max_length=300,
        help_text="""
            Must be in the format https://www.youtube.com/embed/x-xxxxxxxxx
        """
    )
