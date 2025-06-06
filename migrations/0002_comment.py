# Generated by Django 5.2 on 2025-05-03 02:36

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "author_name",
                    models.CharField(max_length=100, verbose_name="Имя автора"),
                ),
                ("content", models.TextField(verbose_name="Текст комментария")),
                (
                    "date_created",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Дата создания"
                    ),
                ),
                (
                    "is_approved",
                    models.BooleanField(default=False, verbose_name="Одобрено"),
                ),
                (
                    "news",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="main.news",
                        verbose_name="Новость",
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий",
                "verbose_name_plural": "Комментарии",
                "ordering": ["-date_created"],
            },
        ),
    ]
