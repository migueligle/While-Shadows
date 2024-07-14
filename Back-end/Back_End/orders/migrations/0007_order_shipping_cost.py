# Generated by Django 4.2.7 on 2024-03-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_orderstatus_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_cost',
            field=models.DecimalField(decimal_places=2, default=4.5, max_digits=10),
        ),
    ]
