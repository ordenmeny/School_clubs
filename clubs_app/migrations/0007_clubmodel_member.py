# Generated by Django 4.2 on 2023-04-23 17:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubs_app', '0006_alter_clubmodel_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubmodel',
            name='member',
            field=models.ManyToManyField(related_name='member_field', to=settings.AUTH_USER_MODEL),
        ),
    ]
