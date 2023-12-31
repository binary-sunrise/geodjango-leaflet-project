# Generated by Django 3.2.23 on 2023-11-24 06:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('file', models.FileField(upload_to='%Y/%m/%d')),
                ('uploaded_date', models.DateField(blank=True, default=datetime.date.today)),
            ],
        ),
    ]
