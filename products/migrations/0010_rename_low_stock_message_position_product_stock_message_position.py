# Generated by Django 3.2.20 on 2023-07-25 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_low_stock_message_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='low_stock_message_position',
            new_name='stock_message_position',
        ),
    ]