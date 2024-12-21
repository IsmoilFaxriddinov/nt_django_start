from django.db import models


def BlogsModel(models.Model):
    totle = models.CharField(max_length=50, null=True, blank=True, default=True)
    content = models.TextField()
    image = models.ImageField(upload_to="blogs")

    class Meta:
        db_table = 'blogs'
    