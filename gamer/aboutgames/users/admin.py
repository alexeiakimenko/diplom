from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name', 'email', 'birthday', 'favorite_game', 'favorite_genre')
    list_display_links = ('id', 'username', 'name')
    search_fields = ('username', 'name')
    list_filter = ('username', 'name')


admin.site.register(Profile, ProfileAdmin)
