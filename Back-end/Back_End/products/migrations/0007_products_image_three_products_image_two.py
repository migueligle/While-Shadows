# Generated by Django 4.2.7 on 2024-02-24 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image_three',
            field=models.BinaryField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='image_two',
            field=models.BinaryField(blank=True, default=None, null=True),
        ),
    ]
