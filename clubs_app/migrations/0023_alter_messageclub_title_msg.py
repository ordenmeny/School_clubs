# Generated by Django 4.2 on 2023-05-08 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs_app', '0022_alter_messageclub_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageclub',
            name='title_msg',
            field=models.CharField(max_length=128, null=True, verbose_name='Заголовок сообщения'),
        ),
    ]
