# Generated by Django 4.2 on 2023-05-01 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs_app', '0012_articleclub'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleclub',
            name='author_club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clubs_app.clubmodel'),
        ),
    ]