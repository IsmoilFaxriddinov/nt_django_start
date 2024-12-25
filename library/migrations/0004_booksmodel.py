# Generated by Django 5.1.4 on 2024-12-25 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_authormodel_book_name_delete_booksmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, null=True)),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('author_book_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.authormodel')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]
