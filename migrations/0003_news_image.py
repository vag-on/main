# Generated by Django 5.2 on 2025-05-03 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="news_images/",
                verbose_name="Изображение",
            ),
        ),
    ]
