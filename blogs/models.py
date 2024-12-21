from django.db import models

# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=150, null=True, default="title", blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='blog')