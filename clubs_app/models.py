from django.db import models
from django.conf import settings


class ClubModel(models.Model):
    types_of_clubs = [
        ("Тип_не_выбран", "Тип клуба:"),
        ("IT", "IT"),
        ("Спорт", "Спорт"),
        ("Литература", "Литература"),
        ("Рисование", "Рисование"),
        ("Культура", "Культура"),
        ("Музыка", "Музыка"),
        ("Видеоигры", "Видеоигры"),
        ("Общение", "Общение"),
        ("Рукоделие", "Рукоделие"),
    ]

    paid_or_free = [
        ("Не_выбрано", "Платно или бесплатно:"),
        ("Платно", "Платно"),
        ("Бесплатно", "Бесплатно")
    ]

    name_club = models.CharField(null=True, blank=True, max_length=30)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type_club = models.CharField(max_length=100, choices=types_of_clubs, default='Тип_не_выбран')
    paid_free = models.CharField(max_length=100, choices=paid_or_free, default='Не_выбрано')
    info_club = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name_club
