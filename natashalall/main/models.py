import os
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

from work.models import Artwork


class SingletonModel(models.Model):
    """An abstract class used for models where only one object.

    E.g. sitewide settings
    """
    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        pass

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class SiteConfig(SingletonModel):

    information = models.TextField(
        help_text=(
            'The main text that appears on the info page. html is allowed.'
        )
    )
    contact_details = models.TextField(
        help_text=(
            'The main text that appears on the contact page. html is allowed.'
        )
    )
    copyright_line = models.CharField(
        max_length=255,
        default='Copyright',
        help_text=(
            'The copyright text that appears in the footer.'
            'E.g. \'Copyright the artist\''
        )
    )
    homepage_artwork = models.OneToOneField(
        Artwork,
        verbose_name='featured homepage artwork',
        null=True,
        on_delete=models.CASCADE,
        help_text=(
            'The large artwork that appears on the homepage.'
            'Note that this uses the first image found (i.e. the one used in'
            'the thumbnail).'
        )
    )

    def __str__(self):
        return 'Site config'


class SocialMediaType(models.Model):
    name = models.CharField(max_length=30)
    css_class = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class SocialMediaLink(models.Model):
    url = models.CharField(max_length=100)
    type = models.ForeignKey(
        SocialMediaType,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{} | {}'.format(self.type, self.url)


"""
The stuff below has been moved, I just can't figure out how to delete properly
"""


def image_filename(instance, filename):
    """
    Used by the ArtworkImage class when uploading image to specify where they
    are stored and how they are named.
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
    artwork = models.ForeignKey(
        Artwork,
        related_name='images',
        on_delete=models.CASCADE
    )
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
