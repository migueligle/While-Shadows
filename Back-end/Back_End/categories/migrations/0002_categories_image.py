# Generated by Django 4.2.7 on 2024-02-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='image',
            field=models.BinaryField(default=None),
        ),
    ]
