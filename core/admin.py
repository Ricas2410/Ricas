from django.contrib import admin
from .models import TeamMember, Testimonial

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'position')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'date')
    search_fields = ('name', 'company')
    list_filter = ('date',)
