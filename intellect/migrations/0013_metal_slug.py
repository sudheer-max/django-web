# Generated by Django 3.0.3 on 2020-03-04 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intellect', '0012_equipment_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='metal',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
