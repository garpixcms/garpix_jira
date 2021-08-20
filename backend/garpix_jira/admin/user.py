from django.contrib import admin
from ..models.user import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_key', 'display_name', 'email', 'server')
    search_fields = ('display_name', 'email')
    readonly_fields = ('display_name', 'email', 'user_key', 'server')
