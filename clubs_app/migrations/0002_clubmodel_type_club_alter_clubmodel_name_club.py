# Generated by Django 4.2 on 2023-04-10 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubmodel',
            name='type_club',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clubmodel',
            name='name_club',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
