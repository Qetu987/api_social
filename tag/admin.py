from django.contrib import admin
from tag.models import Tag

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'text']
    list_display_links = ['id','slug']
    list_search = ['id', 'slug', 'text']