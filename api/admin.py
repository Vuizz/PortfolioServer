from django.contrib import admin
from . import models

admin.site.register(models.Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'type')
    list_filter = ('title', 'type')
    search_fields = ('title', 'type')
    ordering = ['title']
    list_per_page = 10
# Register your models here.

admin.site.register(models.WorkExperiences)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('year', 'company', 'duration', 'position', 'description')
    list_filter = ('year', 'company')
    search_fields = ('year', 'company')
    ordering = ['year']
    list_per_page = 10