# Generated by Django 3.1.5 on 2021-01-10 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='whishlist',
            name='old_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
