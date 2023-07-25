# Generated by Django 3.2.20 on 2023-07-25 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='low_stock_message_position',
            field=models.CharField(choices=[('left', 'Top Left'), ('right', 'Top Right')], default='left', max_length=5),
        ),
    ]
