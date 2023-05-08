from django.db import models
from django.urls import reverse
from django.conf import settings
from ckeditor.fields import RichTextField
import django


class MessageClub(models.Model):
    author_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE, verbose_name='Отправитель')
    club_contains = models.ForeignKey('ClubModel', on_delete=models.CASCADE, verbose_name='Клуб', null=True)
    slug_content = models.SlugField(unique=True, max_length=512)

    title_msg = models.CharField(null=True, blank=False, max_length=128, verbose_name='Заголовок сообщения')
    body_msg = models.TextField(null=True, blank=False, verbose_name='Сообщение')
    date_load = models.DateField(default=django.utils.timezone.now, verbose_name='Дата')

    class Meta:
        verbose_name = 'Сообщения клубов'
        verbose_name_plural = 'Сообщения клубов'

    def get_delete_url(self):
        return reverse('dashboard_app:delete_content',
                       kwargs={'model_name': 'messageclub', 'content_slug': self.slug_content})


class ArticleClubModel(models.Model):
    author_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    club_contains = models.ForeignKey('ClubModel', on_delete=models.CASCADE, null=True)
    slug_content = models.SlugField(max_length=255, unique=True)

    title_article = models.CharField(max_length=128, verbose_name='Заголовок статьи', unique=True, blank=False)
    text_body = RichTextField(blank=False, null=True, verbose_name='Контент статьи')
    image = models.ImageField(upload_to='articles/', null=True, blank=False, verbose_name='Главное изображение статьи')

    def __str__(self):
        return self.title_article

    class Meta:
        verbose_name = 'Статьи клубов'
        verbose_name_plural = 'Статьи клубов'

    def get_absolute_url(self):
        return reverse('clubs_app:detail_articles', kwargs={'slug_article': self.slug_content})

    def get_delete_url(self):
        return reverse('dashboard_app:delete_content',
                       kwargs={'model_name': 'articleclubmodel', 'content_slug': self.slug_content})


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
    slug_club = models.SlugField(max_length=255, unique=True, null=True)

    def __str__(self):
        return self.title_club

    class Meta:
        verbose_name = 'Клубы'
        verbose_name_plural = 'Клубы'
        ordering = ['-id']


class CatClubModel(models.Model):
    cat = models.CharField(max_length=128, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='photos/', null=True)

    def __str__(self):
        return self.cat

    def get_absolute_url(self):
        return reverse('clubs_app:list_club', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категории клубов'
        verbose_name_plural = 'Категории клубов'
