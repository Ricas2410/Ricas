from django.db import models
from django.utils.text import slugify

class CybersecurityService(models.Model):
    """Model for cybersecurity services"""
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class (e.g., fa-shield-alt)")
    image = models.ImageField(upload_to='cybersecurity/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, help_text="Order in which to display this service")

    class Meta:
        verbose_name = "Cybersecurity Service"
        verbose_name_plural = "Cybersecurity Services"
        ordering = ['order']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class CybersecurityFeature(models.Model):
    """Features of a cybersecurity service"""
    service = models.ForeignKey(CybersecurityService, on_delete=models.CASCADE, related_name='features')
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class (e.g., fa-lock)")

    class Meta:
        verbose_name = "Cybersecurity Feature"
        verbose_name_plural = "Cybersecurity Features"

    def __str__(self):
        return f"{self.service.title} - {self.title}"

class CybersecurityTestimonial(models.Model):
    """Testimonials for cybersecurity services"""
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Cybersecurity Testimonial"
        verbose_name_plural = "Cybersecurity Testimonials"

    def __str__(self):
        return f"{self.name} - {self.company}"
