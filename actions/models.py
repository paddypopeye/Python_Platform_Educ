# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Action(models.Model):
 	user = models.ForeignKey(User, related_name='actions', db_index=True)
 	verb = models.CharField(max_length=255)
 	created = models.DateTimeField(auto_now_add=True,db_index=True)
  	target_ct = models.ForeignKey(ContentType, related_name='target_obj', blank=True, null=True)
 	target_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
 	target = GenericForeignKey('target_ct', 'target_id')
 	


 	class Meta:
 		ordering = ['-created']