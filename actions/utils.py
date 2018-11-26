import datetime
from django.contrib.contenttypes.models import ContentType
from .models import Action
from django.utils import timezone


def create_action(user, verb, target=None):
	#check for any similar action made in the last minute
	now = timezone.now()
	last_minute = now - datetime.timedelta(seconds=60)
	#similar_actions = Action.objects.filter(user_id = user.id, verb = verb, timestamp__gte = last_minute)
	
	#f target != None:
		#arget_ct = ContentType.objects.get_for_model(target)
		#similar_actions = similar_actions.filter(target_ct=target_ct,target_id=target.id)
	#f  not similar_actions:
		# no existing actions found
		#ass
	action = Action(user=user, verb=verb, target=target)
	action.save()
	return True
	#return False
	
