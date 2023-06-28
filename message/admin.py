from django.contrib import admin
from message.models import Message, Group


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'text', 'recipient', 'draft', 'is_read', 'date']
    list_display_links = ['id','owner']
    list_search = ['id', 'owner', 'text']

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'is_private', 'draft', 'is_hide']
    list_display_links = ['id','name']
    list_search = ['id', 'name', 'desc', 'is_private']