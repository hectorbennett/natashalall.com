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

def image_filename(instance, filename):
    """
    Used by the artwork class when uploading image to specify where they are
    stored and how they are named.
    """
    print(filename)
    ext = filename.split('.')[-1]
    print(instance.title)
    filename = "%s.%s" % (instance.title, ext)
    return os.path.join('img/artwork', filename)


class Artwork(models.Model):
    title = models.CharField(max_length=100)
    image_original = models.ImageField(upload_to=image_filename)
    image_large = ImageSpecField(source='image_original',
                                 processors=[ResizeToFit(1000, 1000)],
                                 format='JPEG',
                                 options={'quality': 90})
    creation_date = models.DateField()

    def __str__(self):
        return self.title

