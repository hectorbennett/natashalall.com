from django.db import models

class PageContent(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
