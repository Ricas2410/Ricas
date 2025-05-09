from django.contrib import admin
from .models import SiteSettings, BannerImage, HomePageSettings

class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Site Identity', {
            'fields': ('site_name', 'site_logo', 'favicon')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'address', 'business_hours')
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url')
        }),
        ('Footer', {
            'fields': ('footer_text', 'copyright_text')
        }),
        ('SEO', {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        # Check if an instance already exists
        return not SiteSettings.objects.exists()

class BannerImageAdmin(admin.ModelAdmin):
    list_display = ('get_section_display', 'title')
    list_filter = ('section',)

class HomePageSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle')
        }),
        ('Services Section', {
            'fields': ('services_title', 'services_subtitle')
        }),
        ('Education Section', {
            'fields': ('education_title', 'education_subtitle')
        }),
        ('Development Section', {
            'fields': ('development_title', 'development_subtitle')
        }),
        ('Portfolio Section', {
            'fields': ('portfolio_title', 'portfolio_subtitle')
        }),
        ('Testimonials Section', {
            'fields': ('testimonial_title', 'testimonial_subtitle')
        }),
        ('Call to Action Section', {
            'fields': ('cta_title', 'cta_subtitle')
        }),
    )

    def has_add_permission(self, request):
        # Check if an instance already exists
        return not HomePageSettings.objects.exists()

admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(BannerImage, BannerImageAdmin)
admin.site.register(HomePageSettings, HomePageSettingsAdmin)
