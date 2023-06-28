from django.contrib import admin
from photo.models import Photo, Reviews, Like, Reviews_like
from django.utils.safestring import mark_safe


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_image', 'draft', 'owner', 'date']
    list_display_links = ['id','title']
    list_search = ['id', 'title', 'text']
    list_filter = ['draft', 'owner']

    readonly_fields = ('get_image', )
    
    def get_image(self, obj):
        try:
            a = mark_safe(f'<img src={obj.poster.url} width="100" height="110">')
        except:
            a = None
        return a
    get_image.short_description = "Изображение"


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'text', 'tread', 'parent', 'photo', 'date']
    list_display_links = ['id','owner']
    list_search = ['id', 'owner', 'text']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'user']
    list_display_links = ['id','photo']
    list_search = ['id', 'user']


@admin.register(Reviews_like)
class ReviewsLikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'review', 'user']
    list_display_links = ['id','review']
    list_search = ['id', 'user']