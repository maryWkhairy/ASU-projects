# Generated by Django 3.1.5 on 2021-01-10 01:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0012_auto_20210110_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='additem',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='additem',
            name='user_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
