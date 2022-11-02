# Generated by Django 4.1 on 2022-11-02 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
        ('marcas', '0002_auto_20221102_0206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='categorias.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='marcas.marca')),
            ],
        ),
    ]
