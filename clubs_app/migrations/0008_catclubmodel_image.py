# Generated by Django 4.2 on 2023-04-25 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs_app', '0007_clubmodel_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='catclubmodel',
            name='image',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
    ]
