from django.db import models
from django.utils.text import slugify


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('menu.MenuItem', null=True, blank=True,
                               related_name='children', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(MenuItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
