from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class ClubModel(models.Model):
    # manager = models.ForeignKey(get_user_model(), default=get_user_model, null=True, max_length=1024, on_delete=models.CASCADE)
    title_club = models.CharField(max_length=128)
    cat_club = models.ForeignKey('CatClubModel', on_delete=models.CASCADE)
    info_club = models.TextField()
    days_event = models.CharField(max_length=32, null=True)
    time_start_event = models.TimeField(null=True)
    duration_event = models.TimeField(null=True)
    price_club = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.title_club

    class Meta:
        verbose_name = 'Клубы'
        verbose_name_plural = 'Клубы'


class CatClubModel(models.Model):
    cat = models.CharField(max_length=128, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.cat

    class Meta:
        verbose_name = 'Категории клубов'
        verbose_name_plural = 'Категории клубов'
