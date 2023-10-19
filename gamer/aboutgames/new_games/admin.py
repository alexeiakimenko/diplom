from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class NewGameAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = NewGame
        fields = '__all__'


class NewGameAdmin(admin.ModelAdmin):
    form = NewGameAdminForm
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
