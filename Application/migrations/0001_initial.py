# Generated by Django 4.1.7 on 2023-03-29 06:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=10000)),
                ('room', models.CharField(max_length=100)),
                ('sender', models.CharField(max_length=100)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 29, 12, 10, 41, 125594))),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('creater', models.CharField(max_length=100)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 29, 12, 10, 41, 124594))),
            ],
        ),
    ]
