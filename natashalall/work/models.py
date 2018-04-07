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
    creation_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    exhibitions = models.ManyToManyField(
        Exhibition,
        verbose_name='list of exhibitions',
        blank=True,
    )

    def __str__(self):
        return self.title


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
    url = models.CharField(max_length=300, help_text='Must be in the format https://www.youtube.com/embed/x-xxxxxxxxx')
