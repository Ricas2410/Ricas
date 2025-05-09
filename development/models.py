from django.db import models
from django.utils.text import slugify

class DevelopmentService(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    technologies = models.CharField(max_length=255)
    image = models.ImageField(upload_to='development/')
    order = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
