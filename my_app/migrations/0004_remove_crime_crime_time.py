# Generated by Django 4.2.5 on 2023-11-24 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_criminal_criminal_photo_alter_crime_crime_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crime',
            name='crime_time',
        ),
    ]
