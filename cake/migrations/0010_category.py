# Generated by Django 4.2.4 on 2023-09-09 11:24

import cake.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0009_remove_cartitem_cart_remove_cartitem_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=cake.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
