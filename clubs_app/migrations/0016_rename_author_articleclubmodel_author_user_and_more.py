# Generated by Django 4.2 on 2023-05-01 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs_app', '0015_rename_articleclub_articleclubmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articleclubmodel',
            old_name='author',
            new_name='author_user',
        ),
        migrations.RenameField(
            model_name='articleclubmodel',
            old_name='author_club',
            new_name='club_contains',
        ),
    ]