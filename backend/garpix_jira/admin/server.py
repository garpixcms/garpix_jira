from django.contrib import admin
from ..models.server import Server


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('server',)
