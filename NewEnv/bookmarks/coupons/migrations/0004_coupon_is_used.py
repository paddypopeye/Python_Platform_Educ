# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0003_auto_20160706_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='is_used',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
