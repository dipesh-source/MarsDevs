from django.db import models

# Create your models here.
from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Consumer(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="ven")
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.vendor)

<<<<<<< HEAD
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     brand = models.CharField(max_length=100)
#     color = models.CharField(max_length=100)
#     price = models.IntegerField()
#     in_stock = models.BooleanField(default=True)
=======
class Movies_manager(models.Manager):
    def get_queryset(self):
        return super(Movies_manager, self).get_queryset().values_list("name","created")

class Movies(models.Model):
    name = models.CharField(max_length=100)
    hero = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    custome_obj = Movies_manager()

    def __str__(self):
        return self.name


class Viewers(models.Model):
    movies = models.ForeignKey(
        Movies, on_delete=models.SET_NULL, null=True, related_name="movies"
    )
    vname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.movies)
>>>>>>> develop
