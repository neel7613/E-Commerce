# Generated by Django 3.0.8 on 2020-08-13 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20200813_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heavy_machine',
            name='mixing_drum',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
