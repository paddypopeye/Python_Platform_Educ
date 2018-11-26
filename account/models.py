# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.models import User
from friendship.models import Friend


# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	date_of_birth = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
	teacher = models.BooleanField(default=False)

	def __unicode__(self):
		return 'Profile for user {}'.format(self.user.username)

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

class Contact(models.Model):
	user_from = models.ForeignKey(User, related_name='rel_from_set')
	user_to = models.ForeignKey(User, related_name='rel_to_set')
	created = models.DateTimeField(auto_now_add=True, db_index=True)

	class Meta:
		ordering = ('-created',)

	def __unicode__(self):
		return '{} follows {}'.format(self.user_from, self.user_to)

class FirstFriendModel(models.Model):
	users = models.ManyToManyField(User)
	current_user = models.ForeignKey(User, related_name='owner', null=True)
	created = models.DateTimeField(auto_now_add=True)
	#friends = Friend.users.all()
	@classmethod
	def make_friend(cls, current_user, new_friend):
		friend, created = cls.objects.get_or_create(
				current_user=current_user
			)
		friend.users.add(new_friend)

	@classmethod
	def lose_friend(cls, current_user, new_friend):
		friend, created = cls.objects.get_or_create(
				current_user=current_user
			)
		friend.users.remove(new_friend)

#dynamic field added to User 
User.add_to_class('follow', models.ManyToManyField('self', through=Contact,related_name='follower', symmetrical=False))
User.add_to_class('teacher', models.ManyToManyField('self', through=Profile,related_name='teachers', symmetrical=False))



