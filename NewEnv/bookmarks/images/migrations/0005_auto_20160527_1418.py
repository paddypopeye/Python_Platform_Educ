# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_auto_20160525_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='image',
            name='users_like',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='images_liked', blank=True),
        ),
    ]
