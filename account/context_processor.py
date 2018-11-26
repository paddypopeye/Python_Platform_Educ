from friendship.models import Friend, FriendshipRequest
from django.contrib.auth.models import User, AnonymousUser

def friendsProcessor(request):
		try:
		 friends = Friend.objects.friends(request.user)
		 requests = FriendshipRequest.objects.select_related().all()

		 return {'friends': friends, 'requests':requests }
		except:
			return {'friends': '', 'requests': ''}