# Generated by Django 4.1 on 2022-12-23 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Alumno",
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
                ("nombre", models.CharField(max_length=100)),
                ("matricula", models.PositiveIntegerField()),
                ("correo", models.EmailField(max_length=254)),
            ],
        ),
    ]
