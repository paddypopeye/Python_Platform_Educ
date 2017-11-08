from django.contrib import admin
from .models import Subject, Course, Module
from django.contrib.auth.models import Permission


admin.site.register(Permission)

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {'slug': ('title',)}


class ModuleInLine(admin.StackedInline):
	model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ['title', 'subject', 'created', 'id']
	list_filter = ['created', 'subject']
	search_fields = ['title','overview']
	prepopulated_fields = {'slug':('title',)}
	inlines = [ModuleInLine]
