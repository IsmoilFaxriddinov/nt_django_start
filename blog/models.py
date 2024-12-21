from django.db import models

# Create your models here.

class BlogsModel(models.Model):
    title = models.CharField(max_length=150, null=True, default="title", blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'blogs'