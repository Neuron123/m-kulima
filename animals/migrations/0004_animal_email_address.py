# Generated by Django 2.2.7 on 2020-11-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_auto_20201127_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='Email_Address',
            field=models.EmailField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]