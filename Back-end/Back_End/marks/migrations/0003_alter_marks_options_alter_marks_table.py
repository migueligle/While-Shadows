# Generated by Django 4.2.7 on 2024-02-24 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0002_marks_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marks',
            options={'verbose_name': 'marks'},
        ),
        migrations.AlterModelTable(
            name='marks',
            table='marks',
        ),
    ]
