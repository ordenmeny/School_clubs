# Generated by Django 4.2 on 2023-05-01 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubs_app', '0011_clubmodel_slug_club'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleClub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_article', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='articles/')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
