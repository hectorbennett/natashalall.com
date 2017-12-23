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
    filename = "%s.%s" % (title, ext)
    return os.path.join('artwork', filename)


class Artwork(models.Model):
    title = models.CharField(max_length=100)
    creation_date = models.DateField()

    def __str__(self):
        return self.title


class ArtworkImage(models.Model):
    artwork = models.ForeignKey(Artwork, related_name='images')
    image_original = models.ImageField(upload_to=image_filename)
    image_large = ImageSpecField(source='image_original',
                                 processors=[ResizeToFit(1000, 1000)],
                                 format='JPEG',
                                 options={'quality': 90})
    image_medium = ImageSpecField(source='image_original',
                                  processors=[ResizeToFit(500, 500)],
                                  format='JPEG',
                                  options={'quality': 90})

    def get_title(self):
        return self.artwork.title
