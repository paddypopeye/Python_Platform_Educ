# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0002_auto_20160706_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 21, 36, 23, 63587, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='active',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.IntegerField(),
        ),
    ]
