import weasyprint
from io import BytesIO
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from orders.models import Order 


def payment_notification(sender, **kwargs):
	ipn_obj = sender
	if ipn_obj.payment_status == ST_PP_COMPLETED:
		#successful
		order = get_object_or_404(Order, id=ipn_obj.invoice)
		# paid
		order.paid =True
		order.save()
		# invoice e-mail 
		subject = 'Language Course - Invoice No. {}'.format(order.id)
		message = 'Please find attached the invoice for your reservation of a course place.'
		email = EmailMessage(subject, message, 'admin@mysite.com', [order.email])
		# pdf generation 
		html = render_to_string('orders/order/pdf.html', {'order': order})
		out = BytesIO
		stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
		weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
		# pdf attached to email 
		email.attach('order_{}.pdf'.format(order.id), out.getvalue(), 'application/pdf')
		# send e-mail
		email.send()

valid_ipn_received.connect(payment_notification)