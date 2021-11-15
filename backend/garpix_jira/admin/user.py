from django.contrib import admin
from ..models.user import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_key', 'display_name', 'user_tracks_time', 'specialization', 'email', 'server')
    search_fields = ('display_name', 'email')
    readonly_fields = ('display_name', 'email', 'user_key', 'server')
    list_editable = ('user_tracks_time',)
    list_filter = ('user_tracks_time', 'specialization', 'server')
