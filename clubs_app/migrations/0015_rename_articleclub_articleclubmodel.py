# Generated by Django 4.2 on 2023-05-01 17:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubs_app', '0014_alter_articleclub_options_remove_articleclub_text_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArticleClub',
            new_name='ArticleClubModel',
        ),
    ]
