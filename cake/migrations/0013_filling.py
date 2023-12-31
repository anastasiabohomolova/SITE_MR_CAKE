# Generated by Django 4.2.4 on 2023-09-17 09:00

import cake.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0012_alter_info_price_alter_info_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=cake.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('type', models.CharField(default='', max_length=30)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
