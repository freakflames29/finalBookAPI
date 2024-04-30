from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Book(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    buyinglink = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
