# Generated by Django 4.1 on 2023-01-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("book_number", models.IntegerField(default=1, unique=True)),
                ("title", models.CharField(max_length=200)),
                ("author", models.CharField(max_length=200)),
            ],
        ),
    ]
