from django.contrib import admin
from .models import ClubModel, CatClubModel


class ClubModelAdmin(admin.ModelAdmin):
    list_display = ('title_club', 'cat_club')
    list_display_links = ('title_club', 'cat_club')


class CatClubModelAdmin(admin.ModelAdmin):
    list_display = ('cat', 'slug')
    list_display_links = ('cat', 'slug')
    prepopulated_fields = {"slug": ("cat",)}  # автоматически преобразовывать поле name slug из поля name


admin.site.register(ClubModel, ClubModelAdmin)
admin.site.register(CatClubModel, CatClubModelAdmin)
