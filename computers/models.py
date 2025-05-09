from django.db import models
from django.utils.text import slugify

class ComputerCategory(models.Model):
    """Categories for computer products"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='computer_categories/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, help_text="Order in which to display this category")

    class Meta:
        verbose_name = "Computer Category"
        verbose_name_plural = "Computer Categories"
        ordering = ['order']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ComputerProduct(models.Model):
    """Model for computer products"""
    category = models.ForeignKey(ComputerCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='computer_products/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, help_text="Order in which to display this product")

    class Meta:
        verbose_name = "Computer Product"
        verbose_name_plural = "Computer Products"
        ordering = ['order']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class NetworkService(models.Model):
    """Model for network setup services"""
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class (e.g., fa-network-wired)")
    image = models.ImageField(upload_to='network_services/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, help_text="Order in which to display this service")

    class Meta:
        verbose_name = "Network Service"
        verbose_name_plural = "Network Services"
        ordering = ['order']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
