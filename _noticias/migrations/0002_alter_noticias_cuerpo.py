# Generated by Django 4.0.5 on 2022-06-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='cuerpo',
            field=models.TextField(max_length=800),
        ),
    ]
