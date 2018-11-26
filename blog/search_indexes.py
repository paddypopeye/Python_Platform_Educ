import datetime
from haystack import indexes
from .models import Post
from orders.models import Order
from courses.models import Subject, Course, Module

class ModuleIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(model_attr='title')
	description = indexes.CharField(model_attr='description')
	course = indexes.CharField(model_attr='course')

	def get_model(self):
		return Module

	def index_queryset(self, using=None):
		return self.get_model().objects.all()

class CourseIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(model_attr='title')
	created = indexes.DateTimeField(model_attr='created')

	def get_model(self):
		return Course

	def index_queryset(self, using=None):
		return self.get_model().objects.filter(created__lte=datetime.datetime.now())

class SubjectIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(model_attr='title')

	def get_model(self):
		return Subject

	def index_queryset(self, using=None):
		choice = ['English','French','German']
		return self.get_model().objects.filter(title__in=choice)

class PostIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	publish = indexes.DateTimeField(model_attr='publish')

	def get_model(self):
		return Post

	def index_queryset(self, using=None):
		return self.get_model().published.all()


class OrderIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=False)
	created = indexes.DateTimeField(model_attr='created')

	def get_model(self):
		return Order

	def index_queryset(self, using=None):
		return self.get_model().objects.filter(created__lte=datetime.datetime.now())