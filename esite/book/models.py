from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=25)
    author_id = models.ForeignKey('Author', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.title
class Author(models.Model):
    name = models.CharField(max_length=30)
    f_name = models.CharField(max_length=30)
    author_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.f_name