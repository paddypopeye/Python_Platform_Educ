# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Category, Product
from parler.admin import TranslatableAdmin
# Register your models here.

class CategoryAdmin(TranslatableAdmin):
	list_display = ['name', 'slug']
	def get_prepopulated_fields(self, request, obj=None): 
		return {'slug': ('name',)}

class ProductAdmin(TranslatableAdmin):
	list_display = ['name','slug','price','stock','available','created','updated']
	list_filter = ['available', 'created', 'updated']
	list_editable = ['price', 'stock', 'available']
	def get_prepopulated_fields(self, request, obj=None):
		return {'slug':('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)