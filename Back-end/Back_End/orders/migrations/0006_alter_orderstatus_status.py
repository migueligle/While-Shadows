# Generated by Django 4.2.7 on 2024-03-15 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstatus',
            name='status',
            field=models.CharField(max_length=80),
        ),
    ]
