# Generated by Django 5.1.4 on 2024-12-25 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_booksmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('book_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='library.booksmodel')),
            ],
            options={
                'verbose_name': 'Borrower',
                'verbose_name_plural': 'Borrowers',
            },
        ),
    ]
