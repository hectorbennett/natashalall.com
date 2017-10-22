from django.db import models
from django.utils import timezone
from sorl.thumbnail import ImageField

class Artwork(models.Model):
    image = models.ImageField(
        upload_to="artwork/%Y/%m/", blank=True, null=True)
    title = models.CharField(max_length=200)
    medium = models.CharField(max_length=200)
    height = models.IntegerField()
    width = models.IntegerField()
    description = models.TextField()
    date_created = models.DateField()
    date_published = models.DateTimeField(blank=True, null=True,)

    def publish(self):
        self.date_published = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
