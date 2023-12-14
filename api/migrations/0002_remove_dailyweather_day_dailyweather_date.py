# Generated by Django 4.2.7 on 2023-11-07 21:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyweather',
            name='day',
        ),
        migrations.AddField(
            model_name='dailyweather',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
