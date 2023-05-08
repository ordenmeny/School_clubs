from django.contrib import admin
from .models import *


class ClubModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_club', 'cat_club', 'slug_club', 'manager')
    list_display_links = ('title_club', 'cat_club', 'slug_club', 'manager')


class CatClubModelAdmin(admin.ModelAdmin):
    list_display = ('cat', 'slug')
    list_display_links = ('cat', 'slug')
    prepopulated_fields = {"slug": ("cat",)}  # автоматически преобразовывать поле name slug из поля name


class ArticleClubAdmin(admin.ModelAdmin):
    list_display = ('title_article', 'slug_content', 'author_user', 'club_contains')
    list_display_links = ('title_article', 'slug_content', 'author_user', 'club_contains')


class MessageClubAdmin(admin.ModelAdmin):
    list_display = ('author_user', 'club_contains', 'slug_content', 'title_msg', 'body_msg', 'date_load')
    list_display_links = ('author_user', 'club_contains', 'slug_content', 'title_msg', 'body_msg', 'date_load')



admin.site.register(ClubModel, ClubModelAdmin)
admin.site.register(CatClubModel, CatClubModelAdmin)
admin.site.register(ArticleClubModel, ArticleClubAdmin)
admin.site.register(MessageClub, MessageClubAdmin)
