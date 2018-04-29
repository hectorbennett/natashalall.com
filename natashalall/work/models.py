import os

from urllib.parse import urlparse, parse_qs
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
    date = models.DateField(
        help_text='You can just put 01/01/yyyy if you only know the year.',
        null=True
    )
    description = models.TextField(blank=True)
    exhibitions = models.ManyToManyField(
        Exhibition,
        through=Exhibition.artworks.through,
        verbose_name='exhibited in',
        help_text=(
            'Artworks can also be added to exhibitions from the exhibition '
            'edit screen.'
        ),
        blank=True,
    )
    live = models.BooleanField(
        'is live',
        default=True,
        help_text=(
            'If this is unchecked then the artwork will not appear anywhere '
            'on the site.'
        ),
    )

    class Meta:
        ordering = ['-date', 'title']

    @property
    def title_year(self):
        try:
            return ', '.join((str(self.title), str(self.date.year)))
        except:
            return self.title

    @property
    def thumbnail_url(self):
        try:
            tn = self.images.first().image_medium.url
            if tn:
                return tn
        except AttributeError:
            pass

        try:
            tn = self.videos.first().thumbnail_url
            if tn:
                return tn
        except AttributeError:
            pass

        return ''

    def __str__(self):
        return self.title_year


class ArtworkImage(models.Model):
    artwork = models.ForeignKey(
        Artwork,
        related_name='images',
        on_delete=models.CASCADE
    )
    image_original = models.ImageField('image', upload_to=image_filename)
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
    artwork = models.ForeignKey(
        Artwork,
        related_name='videos',
        on_delete=models.CASCADE
    )
    url = models.CharField(
        'youtube url',
        max_length=300,
        help_text=(
            'At the moment this only supports youtube links'
        )
    )

    @property
    def url_id(self):
        u_pars = urlparse(self.url)
        quer_v = parse_qs(u_pars.query).get('v')
        if quer_v:
            return quer_v[0]
        pth = u_pars.path.split('/')
        if pth:
            return pth[-1]

    @property
    def embed_url(self):
        if self.url_id:
            return 'https://www.youtube.com/embed/{}'.format(self.url_id)
        return ''

    @property
    def thumbnail_url(self):
        if self.url_id:
            return 'https://img.youtube.com/vi/{}/mqdefault.jpg'.format(
                self.url_id)
        return ''


class ArtworkAudio(models.Model):
    artwork = models.ForeignKey(
        Artwork,
        related_name='audio_clips',
        on_delete=models.CASCADE
    )
    url = models.CharField(
        'soundcloud url',
        max_length=500,
        help_text=(
            'Must be in iframe format. You can find the '
            'code for this in the embed section of the share dialog in '
            'soundcloud.'
        )
    )
