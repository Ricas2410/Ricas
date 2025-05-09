from django.contrib import admin
from .models import ComputerCategory, ComputerProduct, NetworkService

class ComputerProductInline(admin.TabularInline):
    model = ComputerProduct
    extra = 1

@admin.register(ComputerCategory)
class ComputerCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_featured', 'order')
    list_filter = ('is_featured',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ComputerProductInline]

@admin.register(ComputerProduct)
class ComputerProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_featured', 'order')
    list_filter = ('is_featured', 'category')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(NetworkService)
class NetworkServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'order')
    list_filter = ('is_featured',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
