# Generated by Django 4.2 on 2023-04-22 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs_app', '0002_alter_clubmodel_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatClubModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='clubmodel',
            name='duration_event',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='clubmodel',
            name='time_start_event',
            field=models.TimeField(null=True),
        ),
    ]
