# Generated by Django 5.0.4 on 2024-04-08 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
