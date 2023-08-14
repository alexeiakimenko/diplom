from django.contrib import admin
from .models import *


class NewGameAdmin(admin.ModelAdmin):
    list_display = ('create', 'title', 'genre', 'image', 'video')
    search_fields = ('title', 'genre')
    list_display_links = ('title',)


admin.site.register(NewGame, NewGameAdmin)
admin.site.register(Comments)
