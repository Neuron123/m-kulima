# Generated by Django 2.2.7 on 2020-09-29 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hasianda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Farm_Name', models.CharField(max_length=200)),
                ('County', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('Size', models.CharField(max_length=200)),
                ('Description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
