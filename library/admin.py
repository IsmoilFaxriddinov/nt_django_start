from django.contrib import admin
from . import models

@admin.register(models.BooksModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']

@admin.register(models.AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['author_name']
    search_fields = ['author_name']

@admin.register(models.BorrowersModel)
class BorrowersModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
