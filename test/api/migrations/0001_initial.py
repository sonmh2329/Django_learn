# Generated by Django 4.1.3 on 2022-11-16 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Snippet",
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
                ("code", models.CharField(max_length=50)),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("python", "Python"),
                            ("java", "Java"),
                            ("c++", "C++"),
                        ],
                        default=("python", "Python"),
                        max_length=50,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]