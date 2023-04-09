from django.db import models
from django.conf import settings


class ClubModel(models.Model):
    name_club = models.CharField(max_length=30)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_club
