from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email