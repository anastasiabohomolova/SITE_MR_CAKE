# Generated by Django 4.2.4 on 2023-09-16 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0005_rename_розмір_purchase_вага_alter_purchase_категорія_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='ФІО',
            new_name='ПІБ',
        ),
    ]
