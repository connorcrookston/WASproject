# Generated by Django 2.2 on 2022-03-22 15:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WASapp', '0002_auto_20220322_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='startDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]