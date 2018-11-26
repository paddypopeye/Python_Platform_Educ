# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv, datetime
from django.http import HttpResponse
from django.contrib import admin
from .models import Order, OrderItem
from django.core.urlresolvers import reverse
# Register your models here.

def order_detail(obj):
	return '<a href="{}">View</a>'.format(reverse('orders:admin_order_detail', args=[obj.id]))

order_detail.allow_tags = True

def order_pdf(obj):
	return '<a href="{}">PDF</a>'.format(reverse('orders:admin_order_pdf', args=[obj.id]))

order_pdf.allow_tags = True
order_pdf.short_description = 'PDF bill'

def export_to_csv(modeladmin, request, queryset):
	opts = modeladmin.model._meta
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment;filename={}.csv'.format(opts.verbose_name)
	writer = csv.writer(response)
	fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
	#header information 
	writer.writerow([field.verbose_name for field in fields])
	# write data rows
	for obj in queryset:
		data_row = []
		for field in fields:
			value = getattr(obj, field.name)
			if isinstance(value, datetime.datetime):
				vlaue = value.strftime('%d/%m/%Y')
			data_row.append(value)
		writer.writerow(data_row)
	return response

export_to_csv.short_description = 'Export to CSV'

class OrderItemInline(admin.TabularInline):
	model = OrderItem
	raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
	list_display = ['id','first_name','last_name','email','address','postal_code','city','paid','created','updated', order_detail, order_pdf]
	list_filter = ['paid', 'created', 'updated']
	actions = [export_to_csv]
	inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)



