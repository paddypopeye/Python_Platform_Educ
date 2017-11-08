# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contact',
            name='user_from',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='rel_from_set'),
        ),
        migrations.AddField(
            model_name='contact',
            name='user_to',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='rel_to_set'),
        ),
    ]
