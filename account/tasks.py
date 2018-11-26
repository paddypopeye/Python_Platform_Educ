from celery import task
from django.core.mail import send_mail
from .models import Profile

def profile_created(profile_id):
	profile = Profile.objects.get(id=profile_id)
	subject = 'Order nr. {}'.format(order.id)
	message = 'Dear {},\n\nYou have successfully placed an order.\
	Your profile with id {} and name {}.'.format(profile.first_name,profile.id)
	mail_sent = send_mail(
		subject,message,'admin@myshop.com',
		[profile.email])
	return mail_sent