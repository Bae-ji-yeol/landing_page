from django.db import models


class Translate(models.Model):
    email = models.EmailField(max_length=100)
    title = models.CharField(max_length=100)
    file = models.FileField()
    posted_date = models.DateTimeField(auto_now_add=True)

