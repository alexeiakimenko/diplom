from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import Game, Hint, VideoView,GameComment


class HintAdminForm(forms.ModelForm):
    hint_description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Hint
        fields = '__all__'


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_date')
    list_display_links = ('title',)
    search_fields = ('title',)


class HintAdmin(admin.ModelAdmin):
    form = HintAdminForm
    list_display = ('hint_game', 'hint_title', 'hint_description')
    list_display_links = ('hint_title',)
    search_fields = ('hint_game',)


class VideoViewAdmin(admin.ModelAdmin):
    list_display = ('video_game', 'video_title', 'video_description')
    list_display_links = ('video_title',)
    search_fields = ('video_game',)


admin.site.register(Game, GameAdmin)
admin.site.register(Hint, HintAdmin)
admin.site.register(VideoView,VideoViewAdmin)
admin.site.register(GameComment)
