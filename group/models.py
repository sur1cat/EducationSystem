from django.db import models
from product.models import Product
from user.models import User
from group import constants


class Group(models.Model):
    name = models.CharField(max_length=155)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    min_students = constants.MIN_STUDENTS_IN_A_GROUP
    max_students = constants.MAX_STUDENTS_IN_A_GROUP

    students = models.ManyToManyField(User)
    is_full = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} {self.product}'
