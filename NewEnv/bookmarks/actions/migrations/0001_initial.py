# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('verb', models.CharField(max_length=255)),
                ('target_id', models.PositiveIntegerField(db_index=True, blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('target_ct', models.ForeignKey(to='contenttypes.ContentType', related_name='target_obj', blank=True, null=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
