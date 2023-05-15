from django.db import models


class PersonModel(models.Model):
    name = models.CharField(max_length=128, verbose_name='Ученик', null=True)
    # True - был дежурным. False - не был
    active = models.BooleanField(default=False, verbose_name='Дежурил', null=True)
    date_duty = models.DateTimeField(verbose_name='Дата', null=True)

    class Meta:
        verbose_name = 'Участники'
        verbose_name_plural = 'Участники'

    def __str__(self):
        return self.name
