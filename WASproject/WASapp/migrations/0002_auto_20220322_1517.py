# Generated by Django 2.2 on 2022-03-22 15:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WASapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='startDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]