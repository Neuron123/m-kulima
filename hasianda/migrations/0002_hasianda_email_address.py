# Generated by Django 2.2.7 on 2020-10-01 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hasianda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hasianda',
            name='Email_Address',
            field=models.EmailField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
