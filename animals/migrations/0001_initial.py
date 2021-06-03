# Generated by Django 2.2.7 on 2020-11-25 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date added')),
                ('category', models.CharField(max_length=200)),
                ('animaltype', models.CharField(max_length=200)),
                ('breed', models.CharField(blank=True, max_length=200, null=True)),
                ('number', models.CharField(max_length=200)),
                ('calved', models.BooleanField()),
                ('buyingprice', models.IntegerField(default=0)),
                ('currency', models.CharField(max_length=200)),
                ('Description', models.TextField(blank=True, null=True)),
                ('profilepic', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]
