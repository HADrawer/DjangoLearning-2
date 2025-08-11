from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auther = models.ForeignKey(Author, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True)

class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()