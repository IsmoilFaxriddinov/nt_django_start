from django.contrib import admin
from . import models

@admin.register(models.TeacherModel)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(models.StudentModel)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(models.GroupModel)
class GroupModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(models.LessonModel)
class LessonModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'groups']
    search_fields = ['name']

@admin.register(models.HomeworkModel)
class HomeworkModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'info']
    search_fields = ['info']