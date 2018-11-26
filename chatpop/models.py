# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chatpop(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='msg_sent_from')
    message = models.TextField()
    user_to = models.ForeignKey(User, related_name='msg_sent_to', blank=True, null=True, db_index=True)

    def __unicode__(self):
        return self.message

    