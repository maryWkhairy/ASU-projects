# Generated by Django 3.1.4 on 2021-01-11 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_to_cart',
            name='paid',
        ),
    ]
