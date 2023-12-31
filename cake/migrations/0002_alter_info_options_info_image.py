# Generated by Django 4.2.4 on 2023-08-30 07:55

import cake.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='info',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='info',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=cake.models.upload_location, width_field='width_field'),
        ),
    ]
