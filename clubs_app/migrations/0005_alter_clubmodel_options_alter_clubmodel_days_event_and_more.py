# Generated by Django 4.2 on 2023-04-23 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs_app', '0004_alter_clubmodel_time_event'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clubmodel',
            options={'ordering': ['-id'], 'verbose_name': 'Клубы', 'verbose_name_plural': 'Клубы'},
        ),
        migrations.AlterField(
            model_name='clubmodel',
            name='days_event',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clubmodel',
            name='price_club',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='clubmodel',
            name='time_event',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
