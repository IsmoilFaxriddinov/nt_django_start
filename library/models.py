from django.db import models

class BooksModel(models.Model):
    name = models.CharField(max_length=125, null=True)
    price = models.FloatField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

class AuthorModel(models.Model):
    author_name = models.CharField(max_length=125, null=True)
    book_name = models.ForeignKey(BooksModel, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
