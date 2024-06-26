# Generated by Django 5.0.6 on 2024-05-12 19:52

import django.contrib.postgres.fields.ranges
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', django.contrib.postgres.fields.ranges.DateRangeField()),
            ],
        ),
        migrations.CreateModel(
            name='Caravan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='CaravanImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caravan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caravansApp.caravan')),
            ],
        ),
    ]
