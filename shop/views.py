# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .recommender import Recommender
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.conf import settings
from django.utils import translation
# Create your views here.

def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		language = request.LANGUAGE_CODE
		category = get_object_or_404(Category,translations__language_code=language, translations__slug=category_slug)
		products = products.filter(category=category)
	return render(request, 'shop/product/list.html', 
		{'category': category, 'categories': categories, 'products': products })


def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id,
	translations__slug=slug, available=True)
	cart_product_form = CartAddProductForm()
	r = Recommender()
	recommended_products = r.suggest_products_for([product])
	language = request.LANGUAGE_CODE
	return render(request, 'shop/product/detail.html', 
		{'product': product, 'cart_product_form': cart_product_form, 
		'recommended_products': recommended_products })