from django.db import models
from django.core.exceptions import ValidationError

class SiteSettings(models.Model):
    """Site-wide settings that can be managed by the admin"""
    site_name = models.CharField(max_length=100, default="Ricas IT Services")
    site_logo = models.ImageField(upload_to='site/', help_text="Site logo displayed in the navbar", blank=True, null=True)
    favicon = models.ImageField(upload_to='site/', help_text="Site favicon", blank=True, null=True)

    # Contact Information
    email = models.EmailField(default="services.ricas@gmail.com")
    phone = models.CharField(max_length=20, default="0505584553")
    address = models.CharField(max_length=255, default="Accra, Ghana")
    business_hours = models.CharField(max_length=255, default="Mon-Fri: 9:00 AM - 5:00 PM")

    # Social Media
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    # Footer
    footer_text = models.TextField(default="Providing quality ICT education and professional software development services to help individuals and businesses thrive in the digital world.")
    copyright_text = models.CharField(max_length=255, default="© {year} Ricas IT Services. All rights reserved.")

    # External Links
    ecommerce_url = models.URLField(blank=True, null=True, help_text="URL to the e-commerce website for computer sales")

    # SEO
    meta_description = models.TextField(blank=True, null=True, help_text="Description for search engines")
    meta_keywords = models.CharField(max_length=255, blank=True, null=True, help_text="Keywords for search engines")

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name

    def clean(self):
        # Ensure only one instance of SiteSettings exists
        if SiteSettings.objects.exists() and not self.pk:
            raise ValidationError("There can only be one Site Settings instance")
        return super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class BannerImage(models.Model):
    """Banner images for different sections of the site"""
    SECTION_CHOICES = [
        ('home_hero', 'Home Hero'),
        ('about_hero', 'About Hero'),
        ('education_hero', 'Education Hero'),
        ('development_hero', 'Development Hero'),
        ('portfolio_hero', 'Portfolio Hero'),
        ('contact_hero', 'Contact Hero'),
        ('cybersecurity_hero', 'Cybersecurity Hero'),
        ('computers_hero', 'Computers Hero'),
        ('network_hero', 'Network Services Hero'),
        ('cta_image', 'Call to Action Image'),
        ('about_company', 'About Company Image'),
        ('education_overview', 'Education Overview Image'),
        ('development_overview', 'Development Overview Image'),
        ('cybersecurity_overview', 'Cybersecurity Overview Image'),
        ('computers_overview', 'Computers Overview Image'),
        ('about_cta', 'About CTA Image'),
        ('education_cta', 'Education CTA Image'),
        ('development_cta', 'Development CTA Image'),
        ('portfolio_cta', 'Portfolio CTA Image'),
        ('contact_cta', 'Contact CTA Image'),
        ('cybersecurity_cta', 'Cybersecurity CTA Image'),
        ('computers_cta', 'Computers CTA Image'),
    ]

    section = models.CharField(max_length=50, choices=SECTION_CHOICES, unique=True)
    image = models.ImageField(upload_to='banners/', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Banner Image"
        verbose_name_plural = "Banner Images"

    def __str__(self):
        return self.get_section_display()

class HomePageSettings(models.Model):
    """Settings specific to the home page"""
    hero_title = models.CharField(max_length=100, default="Empowering Through Technology")
    hero_subtitle = models.TextField(default="We provide quality ICT education for all ages and professional software development services tailored to your business needs.")

    services_title = models.CharField(max_length=100, default="Our Services")
    services_subtitle = models.TextField(default="Discover how we can help you or your organization thrive in the digital world")

    education_title = models.CharField(max_length=100, default="ICT Education Services")
    education_subtitle = models.TextField(default="Practical technology education for all ages")

    development_title = models.CharField(max_length=100, default="Software Development Services")
    development_subtitle = models.TextField(default="Custom solutions tailored to your business needs")

    portfolio_title = models.CharField(max_length=100, default="Our Portfolio")
    portfolio_subtitle = models.TextField(default="Check out some of our recent projects")

    testimonial_title = models.CharField(max_length=100, default="What Our Clients Say")
    testimonial_subtitle = models.TextField(default="Testimonials from our satisfied clients")

    cta_title = models.CharField(max_length=100, default="Ready to Transform Your Digital Experience?")
    cta_subtitle = models.TextField(default="Contact us today to discuss your ICT education or software development needs. Our team is ready to help you achieve your goals.")

    class Meta:
        verbose_name = "Home Page Settings"
        verbose_name_plural = "Home Page Settings"

    def __str__(self):
        return "Home Page Settings"

    def clean(self):
        # Ensure only one instance exists
        if HomePageSettings.objects.exists() and not self.pk:
            raise ValidationError("There can only be one Home Page Settings instance")
        return super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
