# Generated by Django 3.2.20 on 2023-08-01 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0002_alter_faqs_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqs',
            name='category',
            field=models.CharField(choices=[('', 'Select Category +'), ('OR', 'Order'), ('DL', 'Delivery'), ('AC', 'Account'), ('PR', 'Product'), ('OT', 'Other')], max_length=2),
        ),
    ]
