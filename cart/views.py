# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from shop.recommender import Recommender
from .forms import CartAddProductForm
from .cart import Cart
from coupons.forms import CouponApplyForm
from django.utils import translation 
from django.conf import settings
# Create your views here.
@require_POST
def cart_add(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	form = CartAddProductForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])

	return redirect('cart:cart_detail')

def cart_remove(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	cart.remove(product)
	if cart:
		return redirect('cart:cart_detail')
	return redirect('/')

def cart_detail(request):
	translation.activate(settings.LANGUAGE_CODE)
	cart = Cart(request)
	for item in cart:
		item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update':True})

	coupon_apply_form = CouponApplyForm()
	r = Recommender()
	cart_products = [item['product'] for item in cart]
	r.products_bought([item['product'] for item in cart])
	recommended_products = r.suggest_products_for(cart_products)
	return render(request, 'cart/Cartdetail.html', {'cart': cart,'recommended_products': recommended_products,'coupon_apply_form': coupon_apply_form, 'cart_products':cart_products })