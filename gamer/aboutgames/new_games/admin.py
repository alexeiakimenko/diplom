from django.contrib import admin
from .models import *


class NewGameAdmin(admin.ModelAdmin):
    list_display = ('create', 'title', 'genre', 'rating_site', 'rating')
    search_fields = ('title', 'genre')
    list_display_links = ('title',)
    readonly_fields = ('rating_site',)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'favourite_game', 'favourite_genre')
    list_display_links = ('name',)


class NewVoteUserAdmin(admin.ModelAdmin):
    list_display = ('user_evaluation', 'game_evaluation', 'evaluation')


admin.site.register(NewGame, NewGameAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(NewVoteUser, NewVoteUserAdmin)
