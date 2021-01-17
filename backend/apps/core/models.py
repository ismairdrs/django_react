from django.contrib.auth.models import User
from django.db import models


class List(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=150)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    done = models.BooleanField(default=True)

    def __str__(self):
        return self.name
