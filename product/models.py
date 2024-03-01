from django.db import models
from user.models import User


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=155)
    start_date = models.DateTimeField()
    price = models.DecimalField()

    def __str__(self):
        return f"{self.name} {self.author}"


class UserProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    student = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.product} {self.student}"
