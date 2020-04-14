# Generated by Django 2.2 on 2020-04-13 06:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20200405_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]