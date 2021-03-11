from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
