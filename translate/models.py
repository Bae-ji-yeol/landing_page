from django.db import models


class Author(models.Model):
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email


class Data(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    file = models.FileField()
    create_date = models.DateTimeField(auto_now_add=True)

