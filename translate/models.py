from django.db import models
from datetime  import datetime


class Author(models.Model):
    email = models.EmailField(max_length=40)
    title = models.CharField(max_length=100)
    file = models.FileField(null=True)
    check1 = models.BooleanField(blank=False)
    check2 = models.BooleanField(blank=False)
    create_date = models.DateTimeField()


