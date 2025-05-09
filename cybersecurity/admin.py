from django.contrib import admin
from .models import CybersecurityService, CybersecurityFeature, CybersecurityTestimonial

class CybersecurityFeatureInline(admin.TabularInline):
    model = CybersecurityFeature
    extra = 1

@admin.register(CybersecurityService)
class CybersecurityServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'order')
    list_filter = ('is_featured',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CybersecurityFeatureInline]

@admin.register(CybersecurityTestimonial)
class CybersecurityTestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'is_featured')
    list_filter = ('is_featured',)
    search_fields = ('name', 'company', 'content')
