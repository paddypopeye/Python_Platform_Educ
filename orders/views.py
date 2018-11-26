# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import weasyprint
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import translation
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from shop.recommender import Recommender
# Create your views here.

@staff_member_required
def admin_order_detail(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	return render(request, 'admin/orders/order/detail.html', {'order': order})

@staff_member_required
def admin_order_pdf(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	html = render_to_string('orders/order/pdf.html', {'order': order})
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="order_{}.pdf"'.format(order.id)
	weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])

	return response


def order_create(request):
	translation.activate(settings.LANGUAGE_CODE)
	cart = Cart(request)
	if request.method == 'POST':
		r = Recommender()
		cart_products = [item['product'] for item in cart]
		print "CART_PRODUCTS", cart_products
		recommended_products = r.suggest_products_for(cart_products,4)
		print 'recommended_product', recommended_products
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save(commit=False)
			order.save()

			if cart.coupon:
				coupon = cart.coupon
				coupon.save()
				order.discount = coupon.discount
				order.save()
			for item in cart:
				OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
			#emptying the cart
			cart.clear()
			#launch celery async task
			order_created.delay(order.id)
			request.session['order_id'] = order.id #set order.id session
			return redirect(reverse('payment:process'))
	else:
	
		form = OrderCreateForm()
		r = Recommender()
		cart_products = [item['product'] for item in cart]
		recommended_products = r.suggest_products_for(cart_products)
	return render(request, 'orders/order/create.html', {'cart': cart, 'form':form, 'recommended_products':recommended_products, 'cart_products': cart_products})