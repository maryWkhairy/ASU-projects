# Generated by Django 3.1.4 on 2021-01-12 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout_details',
            name='count',
        ),
        migrations.RemoveField(
            model_name='checkout_details',
            name='cvv',
        ),
        migrations.RemoveField(
            model_name='checkout_details',
            name='exp',
        ),
        migrations.RemoveField(
            model_name='checkout_details',
            name='name',
        ),
        migrations.RemoveField(
            model_name='checkout_details',
            name='number',
        ),
        migrations.CreateModel(
            name='User_participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
