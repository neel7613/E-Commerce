# Generated by Django 3.0.8 on 2020-08-12 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20200813_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heavy_machine',
            name='image',
            field=models.ImageField(blank=True, default='default.jpeg', null=True, upload_to='machine/'),
        ),
    ]
