from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import Game, Hint, VideoView, GameComment, VoteUser


class HintAdminForm(forms.ModelForm):
    hint_description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Hint
        fields = '__all__'


class GameAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Game
        fields = '__all__'


class GameAdmin(admin.ModelAdmin):
    form = GameAdminForm
    list_display = ('id', 'title', 'genre', 'release_date', 'rating_site', 'rating')
    list_display_links = ('title',)
    readonly_fields = ('rating_site',)
    search_fields = ('title',)


class HintAdmin(admin.ModelAdmin):
    form = HintAdminForm
    list_display = ('hint_game', 'hint_title', 'hint_description')
    list_display_links = ('hint_title',)
    list_filter = ('hint_game',)
    search_fields = ('hint_title',)


class VideoViewAdmin(admin.ModelAdmin):
    list_display = ('video_game', 'video_title', 'video_description')
    list_display_links = ('video_title',)
    search_fields = ('video_title',)
    list_filter = ('video_game',)


class VoteUserAdmin(admin.ModelAdmin):
    list_display = ('user_evaluation', 'game_evaluation', 'evaluation')


admin.site.register(Game, GameAdmin)
admin.site.register(Hint, HintAdmin)
admin.site.register(VideoView, VideoViewAdmin)
admin.site.register(GameComment)
admin.site.register(VoteUser, VoteUserAdmin)
