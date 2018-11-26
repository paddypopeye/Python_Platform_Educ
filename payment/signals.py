import weasyprint
from django.template.loader import render_to_string
from paypal.standard.ipn.signals import valid_ipn_received
from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from django.conf import settings
from django.core.mail import EmailMessage	
from orders.models import Order 
from io import BytesIO

def payment_notification(sender, **kwargs):
	ipn_obj = sender 
	if ipn_obj.payment_status == ST_PP_COMPLETED:
		#successful
		order = get_object_or_404(Order, id=ipn_obj.invoice)
		#paid
		order.paid = True
		order.save()
		#Invoice Email
		subject = 'Shop - Invoice no. {}'.format(order.id)
		message = 'Please, find the invoice for your orders attached'
		email = EmailMessage(subject, message, 'admin@adminshop.com', [order.email])
		# generate PDF file
		html = render_to_string('orders/order/pdf.html', {'order': order})
		out = BytesIO
		stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
		weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
		#attach PDF to email
		email.attach('order_{}.pdf'.format(order.id), out.getvalue(), 'application/pdf')
		# send mail
		email.send()

valid_ipn_received.connect(payment_notification)

