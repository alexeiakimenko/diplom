from django.contrib import admin
from .models import *


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_date')
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(Game, GameAdmin)
