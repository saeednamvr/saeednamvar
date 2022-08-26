from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(default=True)
    created = models.DateTimeField()
    time = models.TimeField()
