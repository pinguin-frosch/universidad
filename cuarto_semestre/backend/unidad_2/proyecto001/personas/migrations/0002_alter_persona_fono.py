# Generated by Django 4.1 on 2022-10-20 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fono',
            field=models.CharField(max_length=15),
        ),
    ]
