from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Article(models.Model):
    article_id = models.BigAutoField(primary_key=True)
    article_ownership = models.ForeignKey(User, on_delete=models.CASCADE)
    article_creation_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300, blank=True, default='')
    tags = models.CharField(max_length=200)
    content = models.TextField()
    last_edit = models.DateField(auto_now=True)
    image = models.ImageField(upload_to ='article_files/')

    def __str__(self):
        return self.title

class Comments(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    comment_ownership = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_creation_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    last_edit = models.DateField(auto_now=True)

    def __str__(self):
        return self.content