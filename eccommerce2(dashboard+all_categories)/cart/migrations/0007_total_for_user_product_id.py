# Generated by Django 3.1.4 on 2021-01-11 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_checkout_details_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='total_for_user',
            name='product_id',
            field=models.CharField(default=0, max_length=100000),
            preserve_default=False,
        ),
    ]
