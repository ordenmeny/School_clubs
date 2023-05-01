from django.contrib import admin
from .models import ClubModel, CatClubModel, ArticleClubModel


class ClubModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_club', 'cat_club', 'slug_club')
    list_display_links = ('title_club', 'cat_club', 'slug_club')


class CatClubModelAdmin(admin.ModelAdmin):
    list_display = ('cat', 'slug')
    list_display_links = ('cat', 'slug')
    prepopulated_fields = {"slug": ("cat",)}  # автоматически преобразовывать поле name slug из поля name


class ArticleClubAdmin(admin.ModelAdmin):
    list_display = ('title_article', 'slug', 'author_user', 'club_contains')
    list_display_links = ('title_article', 'slug', 'author_user', 'club_contains')


admin.site.register(ClubModel, ClubModelAdmin)
admin.site.register(CatClubModel, CatClubModelAdmin)
admin.site.register(ArticleClubModel, ArticleClubAdmin)
