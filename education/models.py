from django.db import models
from django.utils.text import slugify

class EducationService(models.Model):
    AGE_GROUP_CHOICES = [
        ('kids', 'Kids (6-12)'),
        ('teens', 'Teens (13-17)'),
        ('adults', 'Adults (18+)'),
        ('all', 'All Ages'),
    ]

    FORMAT_CHOICES = [
        ('in_person', 'In-Person'),
        ('online', 'Online'),
        ('hybrid', 'Hybrid'),
    ]

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    age_group = models.CharField(max_length=20, choices=AGE_GROUP_CHOICES)
    learning_goals = models.TextField()
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES)
    image = models.ImageField(upload_to='education/')
    order = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
