# Generated by Django 2.2.7 on 2020-10-11 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hasianda', '0005_auto_20201003_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hasianda',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='farmlist', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
