# Generated by Django 4.2.7 on 2023-12-10 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_dailyweather_city_alter_hourlyweather_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherinfo',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
