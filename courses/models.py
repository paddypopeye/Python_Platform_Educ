# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .fields import OrderField
from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.

class Subject(models.Model):
	title = models.CharField(_('title'),max_length=200)
	slug = models.SlugField(max_length=250, unique=True)

	class Meta:
		ordering = ('-title',)
	
	def __unicode__(self):
		return self.title

class Course(models.Model):
	owner = models.ForeignKey(User, related_name='courses_created')
	subject = models.ForeignKey(Subject, related_name='courses')
	title = models.CharField(_('title'),max_length=200)
	slug = models.SlugField(_('slug'),max_length=200, unique=True)
	overview = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	student = models.ManyToManyField(User, related_name='courses_joined', blank=True)

	class Meta:
		ordering = ('-created',)

	def __unicode__(self):
		return self.title

class Module(models.Model):
	course = models.ForeignKey(Course, related_name='modules')
	title = models.CharField(_('title'),max_length=200)
	description = models.TextField(blank=True)
	order = OrderField(blank=True, for_fields=['course'], default=1)

	class Meta:
		ordering = ['order']

	def __unicode__(self):
		return '{}. {}'.format(self.order, self.title)


class Content(models.Model):
	module = models.ForeignKey(Module, related_name='contents')
	content_type = models.ForeignKey(ContentType, limit_choices_to={'model__in':('text','video','image','file')})
	object_id = models.PositiveIntegerField()
	item = GenericForeignKey('content_type', 'object_id')
	order = OrderField(blank=True, for_fields=['module'], default=1)
	
	class Meta:
		ordering = ['order']

class ItemBase(models.Model):
	owner = models.ForeignKey(User, related_name='%(class)s_related')
	title = models.CharField(_('title'),max_length=250)
	updated = models.DateTimeField(auto_now=True)

	def render(self):
		return render_to_string('courses/content/{}.html'.format(self._meta.model_name),{'item':self})
	
	class Meta:
		abstract = True

	def __unicode__(self):
		return self.title

class Text(ItemBase):
	content = models.TextField()

class File(ItemBase):
	file = models.FileField(upload_to='files')

class Image(ItemBase):
	file = models.FileField(upload_to='images')

class Video(ItemBase):
	url = models.URLField()