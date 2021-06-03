# Generated by Django 2.2.7 on 2020-10-11 18:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date added')),
                ('Crop_Name', models.CharField(max_length=200)),
                ('Crop_Variety', models.CharField(max_length=200)),
                ('Date_Of_Planting', models.DateTimeField(default=datetime.datetime.now, verbose_name='date planted')),
                ('Expected_Date_Of_Havest', models.DateTimeField(default=datetime.datetime.now, verbose_name='estimated havest date')),
                ('Quantity_Of_Seeds', models.CharField(max_length=200)),
                ('Cost_Of_Seeds', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Email_Address', models.EmailField(max_length=1000)),
            ],
        ),
    ]
