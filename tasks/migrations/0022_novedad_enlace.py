# Generated by Django 3.2.16 on 2023-05-28 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0021_remove_novedad_enlace'),
    ]

    operations = [
        migrations.AddField(
            model_name='novedad',
            name='enlace',
            field=models.URLField(blank=True, null=True),
        ),
    ]
