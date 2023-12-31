# Generated by Django 4.2.5 on 2023-11-14 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_alter_crime_crime_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminal',
            name='criminal_photo',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='crime',
            name='crime_time',
            field=models.IntegerField(),
        ),
    ]
