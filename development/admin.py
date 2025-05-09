from django.contrib import admin
from .models import DevelopmentService

@admin.register(DevelopmentService)
class DevelopmentServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description', 'technologies')
    prepopulated_fields = {'slug': ('title',)}
