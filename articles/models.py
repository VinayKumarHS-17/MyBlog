from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    Category_name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.Category_name
    

class Author(models.Model):
    author_name=models.CharField(max_length=20)
    country=models.CharField(max_length=15)

    def __str__(self):
        return self.author_name


class Article(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title