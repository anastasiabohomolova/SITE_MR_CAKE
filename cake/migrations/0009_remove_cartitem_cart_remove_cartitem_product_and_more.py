# Generated by Django 4.2.4 on 2023-09-06 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0008_remove_cart_created_at_remove_cart_items_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
