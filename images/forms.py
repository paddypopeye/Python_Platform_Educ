import urllib 
from django.core.files.base import ContentFile
from django.utils.text import slugify
from django import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ('title', 'url', 'description')
		widgets = { 'url': forms.HiddenInput }

	def clean_url(self):
		url = self.cleaned_data['url']
		valid_extensions = ['tiff','jpeg','jpg', 'gif','png']
		extension = url.rsplit('.', 1)[1].lower()
		if extension not in valid_extensions:
			raise forms.ValidationError('The given url\'s do not match')
		return url

	def save(self, force_insert=False, force_update=False, commit=True):
		image = super(ImageCreateForm, self).save(commit=False)
		image_url = self.cleaned_data['url']
		image_name = '{}.{}'.format(slugify(image.title),image_url.rsplit('.', 1)[1].lower())

		response = urllib.urlopen(image_url) 
		image.image.save(image_name, ContentFile(response.read()), save=False)

		if commit:
			image.save()
		return image
