# Generated by Django 2.2.7 on 2020-10-03 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hasianda', '0003_hasianda_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='hasianda',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='farmlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
