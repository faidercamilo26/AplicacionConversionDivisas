# Generated by Django 4.2.6 on 2023-10-24 19:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipocambio',
            name='fecha_actualizacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
