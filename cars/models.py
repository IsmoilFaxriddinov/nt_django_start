from django.db import models


class CarsModel(models.Model):
    name = models.CharField(max_length=24, null=True)
    description = models.TextField()
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='cars/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'cars'