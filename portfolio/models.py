from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('mobile', 'Mobile App'),
        ('desktop', 'Desktop Application'),
        ('game', 'Game Development'),
        ('education', 'Educational Project'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    client = models.CharField(max_length=100)
    technologies = models.CharField(max_length=255)
    completion_date = models.DateField()
    image = models.ImageField(upload_to='portfolio/')
    order = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-completion_date', 'order']

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/gallery/')
    caption = models.CharField(max_length=255, blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.project.title} - Image {self.order}"

    class Meta:
        ordering = ['order']
