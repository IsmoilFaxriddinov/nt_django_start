# Generated by Django 5.1.4 on 2024-12-25 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_authormodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authormodel',
            name='book_name',
        ),
        migrations.DeleteModel(
            name='BooksModel',
        ),
    ]