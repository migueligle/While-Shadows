# Generated by Django 4.2.7 on 2024-02-24 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_alter_categories_options_alter_categories_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'category'},
        ),
        migrations.AlterModelTable(
            name='categories',
            table='categories',
        ),
    ]
