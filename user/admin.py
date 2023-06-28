from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.safestring import mark_safe


User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('Profile data', {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'bio', 'avatar', 
                                      'get_avatar', 'background', 'get_background')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        ('Tags', {'fields': ('tag',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'bio', 'get_avatar', 'get_background')

    readonly_fields = ('get_avatar', 'get_background')
    
    def get_avatar(self, obj):
        try:
            a = mark_safe(f'<img src={obj.avatar.url} width="100" height="110">')
        except:
            a = None
        return a
    get_avatar.short_description = "Аватар"

    def get_background(self, obj):
        try:
            a = mark_safe(f'<img src={obj.background.url} width="100" height="110">')
        except:
            a = None
        return a
    get_background.short_description = "Задний фон"