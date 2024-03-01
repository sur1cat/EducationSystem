from django.db import models
from product.models import Product


class Lesson(models.Model):
    name = models.CharField(max_length=155)
    link_to_video = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} {self.link_to_video}"
