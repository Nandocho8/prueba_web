# Generated by Django 4.0.5 on 2022-06-30 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='altura',
            field=models.FloatField(verbose_name='altura'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='peso',
            field=models.FloatField(verbose_name='peso'),
        ),
    ]
