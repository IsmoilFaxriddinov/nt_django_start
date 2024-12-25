from django.contrib import admin
from . import models

@admin.register(models.BooksModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']
