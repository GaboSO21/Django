from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # Displayed fields on top bar
    list_display = ('title', 'author', 'published', 'post_categories')
    # Order by selected fields
    ordering = ('author', 'published')
    # Search-able fields within search bar
    search_fields = ('title', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    # Add fields to filters
    list_filter = ('author__username', 'categories__name')

    # Self defined method to show in list_display
    def post_categories(self, obj):
        return ', '.join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description = 'Categories'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

