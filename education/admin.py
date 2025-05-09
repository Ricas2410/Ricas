from django.contrib import admin
from .models import EducationService

@admin.register(EducationService)
class EducationServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'age_group', 'format', 'order')
    list_editable = ('order',)
    list_filter = ('age_group', 'format')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
