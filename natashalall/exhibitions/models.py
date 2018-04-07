from django.db import models


class Exhibition(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    artworks = models.ManyToManyField(
        'work.Artwork',
        verbose_name='exhibited artworks',
        help_text="""
            Artworks can also be added to exhibitions from the artwork edit
            screen.
        """
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date', 'title']

    def _get_title_and_year(self):
        "Returns the title and year."
        return ', '.join((str(self.title), str(self.date.year)))

    title_and_year = property(_get_title_and_year)
