from celery import task
from django.core.mail import send_mail
from .models import Order
from bookmarks import celery

def order_created(order_id):
	order = Order.objects.get(id=order_id)#
	subject =  'Order nr. {}'.format(order_id)
	message = 'Dear {},\n\nYou have successfully placed an order. Your order is {}.'.format(order.first_name, order.id)
	mail_sent  = send_mail(subject, message, 'admin@mysite.com,[order.email]')
	return mail_sent

