import os
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class PageContent(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Shows(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class SocialMediaLinks(models.Model):
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=100)


"""
The stuff below has been moved, I just can't figure out how to delete properly
"""


def image_filename(instance, filename):
    """
    Used by the ArtworkImage class when uploading image to specify where they are
    stored and how they are named.
    """
    ext = filename.split('.')[-1]
    title = instance.get_title()
    filename = "%s.%s" % (title, ext)
    return os.path.join('img/artwork', filename)

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
                                 processors=[ResizeToFit(300, 300)],
                                 format='JPEG',
                                 options={'quality': 90})

    def get_title(self):
        return self.artwork.title
