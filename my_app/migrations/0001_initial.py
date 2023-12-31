# Generated by Django 4.2.5 on 2023-10-03 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crime_date', models.DateField()),
                ('crime_time', models.IntegerField()),
                ('offence', models.CharField(max_length=14)),
                ('location', models.CharField(max_length=23)),
            ],
        ),
        migrations.CreateModel(
            name='Criminal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criminal_name', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=12)),
                ('age', models.IntegerField()),
                ('next_of_kin', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Offence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offence_name', models.CharField(max_length=21)),
                ('penalty', models.CharField(max_length=25)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Witness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('witness_name', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=24)),
                ('contact', models.CharField(max_length=13)),
                ('crime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.crime')),
            ],
        ),
        migrations.CreateModel(
            name='Casuality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casuality_name', models.CharField(max_length=24)),
                ('gender', models.CharField(max_length=24)),
                ('effect', models.CharField(max_length=22)),
                ('crime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.crime')),
            ],
        ),
    ]
