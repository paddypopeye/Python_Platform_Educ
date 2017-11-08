from django.contrib import admin
from .models import Image
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
	list_display = ['title','slug','image','created','id']
	list_filter = ['created', 'slug','url','id']

admin.site.register(Image,ImageAdmin)
