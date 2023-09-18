# Generated by Django 4.2.4 on 2023-09-17 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0011_alter_info_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='info',
            name='type',
            field=models.CharField(choices=[('Торти на день народження', 'the a birthday'), ('Дитячі торти', 'kids'), ('Весільні торти', 'wedding'), ('Корпоративні торти', 'corporate'), ('Кейк-попси', 'cake-pops'), ('Макаруни', 'macaroons')], default='', max_length=30),
        ),
    ]