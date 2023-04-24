from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings


class ClubModel(models.Model):
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, null=True, related_name='user_system')
    title_club = models.CharField(max_length=128, null=False, blank=False)
    cat_club = models.ForeignKey('CatClubModel', on_delete=models.CASCADE)
    info_club = models.TextField()
    days_event = models.CharField(max_length=100, null=True, blank=True)
    time_event = models.CharField(max_length=100, null=True, blank=True)
    price_club = models.CharField(max_length=256, null=True, blank=True)
    member = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='member_field')

    def __str__(self):
        return self.title_club

    class Meta:
        verbose_name = 'Клубы'
        verbose_name_plural = 'Клубы'
        ordering = ['-id']


class CatClubModel(models.Model):
    cat = models.CharField(max_length=128, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.cat

    class Meta:
        verbose_name = 'Категории клубов'
        verbose_name_plural = 'Категории клубов'
