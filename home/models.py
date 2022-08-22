from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    created = models.DateTimeField()